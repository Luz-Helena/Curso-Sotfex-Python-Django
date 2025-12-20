from django.urls import path
from .views import ListaTarefasAPIView, TarefaEstatisticasView
from .views import ListaTarefasAPIView, TarefaEstatisticasView, TarefaDuplicarAPIView, TarefaConcluirTodasAPIView, MeView, ChangePasswordView, StatsView


app_name = 'core'
urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/estatisticas/', TarefaEstatisticasView.as_view(),
         name='tarefas-estatisticas'),
    path('tarefas/<int:pk>/duplicar/',
         TarefaDuplicarAPIView.as_view(), name='tarefa-duplicar'),
    path('tarefas/concluir-todas/', TarefaConcluirTodasAPIView.as_view(),
         name='tarefas-concluir-todas'),
    path('me/', MeView.as_view(), name='me'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('tarefas/<int:pk>/duplicar/',
         TarefaDuplicarAPIView.as_view(), name='tarefa-duplicar'),
    path('tarefas/concluir-todas/', TarefasConcluirTodasAPIView.as_view(),
         name='tarefas-concluir-todas'),
    path('tarefas/<int:pk>/', TarefaDetalheAPIView.as_view(), name='detalhe-tarefa'),
]
