from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('get_board_content/', views.get_board_content, name='get_board_content'),
    path('board_create/', views.board_create, name='board_create'),
    path('list_create/', views.list_create, name='list_create'),
    path('task_create/', views.task_create, name='task_create'),
    path('update_task/', views.update_task, name='update_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    # URL для оновлення даних про завдання
]

app_name = 'boards'