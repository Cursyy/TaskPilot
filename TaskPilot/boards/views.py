from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import *

def board_list(request):
    boards = Board.objects.all()
    return render(request, 'boards/board_list.html', {'boards': boards})

def board_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        board = Board.objects.create(
            name = name,
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def get_board_content(request):
    if request.method == 'GET':
        board_name = request.GET.get('board_name')
        try:
            board = Board.objects.get(name=board_name)
            lists = List.objects.filter(board_name=board)
            lists_html = ""
            for list in lists:
                tasks = Task.objects.filter(list_name=list.name)  # Отримуємо таски для поточного списку
                tasks_html = ""  # Зберігатиме HTML для тасків
                for task in tasks:
                    tasks_html += f'<div class="task_item"><div class="task_title">{task.title}</div><div class="task_description">{task.description}</div><div class="task_end_date">{task.end_date}</div></div>'
                lists_html += f'<div class="list_item"><div class="list_header"><div class="list_title">{list.name}</div><button class="create_task" id="create_task">Add task</button></div><div class="tasks">{tasks_html}</div></div>'
            return JsonResponse({'success': True, 'lists_html': lists_html})
        except Board.DoesNotExist:
            return JsonResponse({'error': 'Дошка з такою назвою не знайдена'}, status=404)
    else:
        return JsonResponse({'error': 'Метод не підтримується'}, status=405)

def list_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        board_name = request.POST.get('board_name')  # Отримання назви поточної дошки
        list = List.objects.create(
            name=name,
            board_name=board_name,
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def task_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        end_date = request.POST.get('end_date')
        list_name = request.POST.get('list_name')  # Отримання назви списку, в якому створюється таск

        task = Task.objects.create(
            title=title,
            description=description,
            end_date=end_date,
            list_name=list_name,  # Запис назви списку в об'єкт таску
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def edit_task(request, task_id):
    if request.method == 'POST':
        # Отримуємо дані про таск з POST-запиту
        title = request.POST.get('title')
        description = request.POST.get('description')
        end_date = request.POST.get('end_date')

        # Знаходимо таск за його ID
        task = get_object_or_404(Task, id=task_id)

        # Оновлюємо дані таску
        task.title = title
        task.description = description
        task.end_date = end_date
        task.save()

        # Повертаємо успішну відповідь
        return JsonResponse({'success': True})
    else:
        # Якщо метод не POST, повертаємо помилку
        return JsonResponse({'error': 'Метод не підтримується'}, status=405)

def delete_task(request, task_id):
    if request.method == 'POST':
        # Знаходимо таск за його ID
        task = get_object_or_404(Task, id=task_id)

        # Видаляємо таск
        task.delete()

        # Повертаємо успішну відповідь
        return JsonResponse({'success': True})
    else:
        # Якщо метод не POST, повертаємо помилку
        return JsonResponse({'error': 'Метод не підтримується'}, status=405)


def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

