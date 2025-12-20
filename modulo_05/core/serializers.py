from rest_framework import serializers
from .models import Tarefa
from django.utils import timezone
from datetime import date


class TarefaSerializer(serializers.ModelSerializer):
    """
    Serializer para o Model Tarefa.
    Responsabilidades:
    1. Converter Tarefa → JSON (serialização)
    2. Converter JSON → Tarefa (desserialização)
    3. Validar dados de entrada
    """

    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo',
                  'concluida', 'criada_em', 'prioridade']
        # Campos gerados automaticamente (não aceitos na entrada)
        read_only_fields = ['id', 'criada_em']

    def validate_titulo(self, value):

        value = value.strip()

        # Validação 1: Não vazio
        if not value:
            raise serializers.ValidationError(
                "O título não pode ser vazio ou conter apenas espaços."
            )

        # Validação 2: Mínimo de caracteres
        if len(value) < 3:
            raise serializers.ValidationError(
                "O título deve ter pelo menos 3 caracteres."
            )

        # Validação 3: Não apenas números
        if value.isdigit():
            raise serializers.ValidationError(
                "O título não pode conter apenas números."
            )

        return value

    def validate(self, attrs):
        request = self.context.get('request')
        is_patch = request and request.method == 'PATCH'
        prioridade = attrs.get('prioridade', getattr(
            self.instance, 'prioridade', None))
        concluida = attrs.get('concluida', getattr(
            self.instance, 'concluida', None))
        if is_patch and prioridade == 'alta' and concluida and (self.instance and not self.instance.concluida):
            raise serializers.ValidationError(
                'Tarefas de prioridade "alta" só podem ser concluídas via PUT.')
        return attrs

    def create(self, validated_data):
        # Exercício 1: Lógica de preenchimento/limpeza de concluido_em na criação
        concluida = validated_data.get('concluida', False)
        if concluida:
            validated_data['data_conclusao'] = timezone.now()
        else:
            validated_data['data_conclusao'] = None
        return super().create(validated_data)

    def validate(self, data):
        prazo = data.get('prazo')
        concluida = data.get('concluida', False)
        request = self.context.get('request')

        if prazo and prazo < date.today():
            raise serializers.ValidationError(
                {'prazo': 'O prazo não pode ser uma data no passado.'}
            )

        if not concluida and prazo is None:
            raise serializers.ValidationError(
                {'prazo': 'O prazo é obrigatório quando a tarefa não está concluída.'}

            )

        metodo = request.method if request else None

        prioridade = data.get(
            'prioridade',
            getattr(self.instance, 'prioridade', None)
        )

        if (
                prioridade == 'alta'
                and concluida is True
                and metodo == 'PATCH'
        ):
            raise serializers.ValidationError({
                'concluida': 'Tarefas com prioridade ALTA só podem ser concluídas via PUT.'
            })

        prioridade_atual = self.instance.prioridade

        if (
                prioridade_atual == 'alta'
                and 'prioridade' in data
                and metodo == 'PATCH'
        ):
            raise serializers.ValidationError({
                'prioridade': 'A prioridade de uma tarefa ALTA não pode ser alterada via PATCH.'
            })

        concluida_atual = (concluida

                           if concluida is not None
                           else getattr(self.instance, 'concluida', False)
                           )

        if concluida_atual:
            data['data_conclusao'] = date.today()
        else:
            data['data_conclusao'] = None
        return data
