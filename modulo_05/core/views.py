from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.db.models import Count, Q
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import date


class ListaTarefasAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):

        # 1. INSTANCIAR: Criar serializer com dados recebidos
        serializer = TarefaSerializer(data=request.data)

        # 2. VALIDAR: Checar se os dados são válidos
        if serializer.is_valid():
            # 3. SALVAR: Persistir no banco de dados
            serializer.save()

        # 4. RESPONDER: Retornar objeto criado + status 201
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        # 5. ERRO: Retornar erros de validação + status 400
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TarefaEstatisticasView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tarefas_agregadas = Tarefa.objects.aggregate()

        total = tarefas_agregadas['total']
        concluidas = tarefas_agregadas['concluidas']
        pendentes = tarefas_agregadas['pendentes']

        taxa_conclusao = (concluidas / total)

        data = {
            "total": total,
            "concluidas": concluidas,
            "pendentes": pendentes,
            "taxa_conclusao": round(taxa_conclusao, 2)
        }

        return Response(data, status=status.HTTP_200_OK)


class TarefaDuplicarAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
        nova_tarefa = Tarefa.objects.create(
            user=request.user,
            titulo=tarefa.titulo + " (Cópia)",
            concluida=False,
            prioridade=tarefa.prioridade
        )
        serializer = TarefaSerializer(nova_tarefa)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TarefaConcluirTodasAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, format=None):
        tarefas = Tarefa.objects.filter(user=request.user, concluida=False)
        tarefas.update(concluida=True, concluido_em=timezone.now())
        return Response({'detail': f'{tarefas.count()} tarefas concluídas.'}, status=status.HTTP_200_OK)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
            'date_joined': user.date_joined
        })


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if not user.check_password(old_password):
            return Response({'error': 'Senha atual incorreta'}, status=400)
        user.set_password(new_password)
        user.save()
        return Response({'detail': 'Senha alterada com sucesso'})


class StatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total = Tarefa.objects.filter(user=request.user).count()
        concluidas = Tarefa.objects.filter(
            user=request.user, concluida=True).count()
        pendentes = Tarefa.objects.filter(
            user=request.user, concluida=False).count()
        taxa_conclusao = concluidas / total if total > 0 else 0
        return Response({
            "total_tarefas": total,
            "concluidas": concluidas,
            "pendentes": pendentes,
            "taxa_conclusao": round(taxa_conclusao, 2)
        })


class TarefaDuplicarAPIView(APIView):
    def post(self, request, pk):
        tarefa_original = get_object_or_404(Tarefa, pk=pk)

        nova_tarefa = Tarefa.objects.create(
            titulo=tarefa_original.titulo + " (cópia)",
            concluida=False,
            data_conclusao=None
        )

        serializer = TarefaSerializer(nova_tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TarefasConcluirTodasAPIView(APIView):
    def patch(self, request):
        hoje = date.today()

        Tarefa.objects.update(concluida=True, data_conclusao=hoje)

        return Response(
            {"mensagem": "Todas as tarefas foram concluídas."},
            status=status.HTTP_200_OK
        )


class TarefaDetalheAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Tarefa, pk=pk)

    def get(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):

        tarefa = self.get_object(pk)

        serializer = TarefaSerializer(
            tarefa,
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(
            tarefa,
            data=request.data,
            partial=True,
            context={'request': request}
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
