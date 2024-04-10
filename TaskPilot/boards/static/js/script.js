let upper_nav = document.querySelector('.upper_nav');
let create_board_btn = document.querySelector('.create_board_btn');
window.addEventListener('resize', function() {
    if (upper_nav.offsetWidth < 200) {
        upper_nav.style.flexDirection = 'column';
        upper_nav.style.alignItems = 'center';
        create_board_btn.style.marginTop = '10px';
    } else {
        upper_nav.style.flexDirection = 'row';
        upper_nav.style.alignItems = 'space-between';
        create_board_btn.style.marginTop = '0';
    }
});


$(document).ready(function() {
    $('#create_board_btn').click(function() {
        $('#create_board_popup').show();
    });

    $(document).on('click', function(event) {
        if (!$(event.target).closest('#create_board_popup').length && !$(event.target).is('#create_board_btn')) {
            $('#create_board_popup').hide();
        }
    });

    $('#create_board_form').submit(function(event) {
        event.preventDefault();
        var boardName = $('#board_name').val();
        var regex = /^[a-zA-Z0-9\s]*$/;
        if(!regex.test(boardName)) {
            $('#board_name').val('');
            $('#board_name').attr('placeholder', 'Invalid board name');
            $('#board_name').css('border', '1px solid red');
        }
        else{
            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            $.ajax({
                type: 'POST',
                url: 'board_create/',
                headers: { "X-CSRFToken": csrftoken },
                data: {
                    'name': boardName,
                    // Додайте інші дані, якщо необхідно
                },
                success: function(data) {
                    $('#create_board_popup').hide();
                    // Оновити список дошок
                    $('#boards_container').append('<button class="board_btn">' + boardName + '</button>');
                }
            });
        }
    });

    $(document).on('click', '.board_btn', function() {
        var boardName = $(this).text(); // Отримання назви дошки з кнопки
        $.ajax({
            url: '/boards/get_board_content/',
            type: 'GET',
            data: {
                board_name: boardName // Передача назви дошки у запиті
            },
            success: function(data) {
                $("#board_content").html(data.lists_html);
                $('#board_title').text(boardName); // Встановлення назви дошки у заголовку
                $('#create_list_btn').remove(); // Видалення попередньої кнопки "Створити список", якщо вона вже існує
                $('.board_header').append('<button id="create_list_btn" class="create_list_btn" >Create list</button>'); // Додавання нової кнопки "Створити список"                
            }
        });
    });

    $(document).on('click', '#create_list_btn', function() {
        $('#create_list_popup').show();
    });

    $(document).on('click', function(event) {
        if (!$(event.target).closest('#create_list_popup').length && !$(event.target).is('#create_list_btn')) {
            $('#create_list_popup').hide();
        }
    });

    $('#create_list_form').submit(function(event) {
        event.preventDefault();
        var listName = $('#list_name').val();
        var boardName = $('#board_title').text(); // Отримання назви поточної дошки
        var regex = /^[a-zA-Z0-9\s]*$/;
        if (!regex.test(listName)) {
            $('#list_name').val('');
            $('#list_name').attr('placeholder', 'Invalid list name');
            $('#list_name').css('border', '1px solid red');
        } else {
            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            $.ajax({
                type: 'POST',
                url: 'list_create/',
                headers: { "X-CSRFToken": csrftoken },
                data: {
                    'name': listName,
                    'board_name': boardName, // Передача назви поточної дошки
                },
                success: function(data) {
                    $('#create_list_popup').hide();
                    // Оновити список списків
                    $('#board_content').append('<div class="list_item"><div class="list_header"><div class="list_title">' + listName + '</div><button class="create_task" id="create_task">Add task</button></div><div class="tasks"></div></div>');
                }
            });
        }
    });

    $(document).on('click', '#create_task', function() {
        var listName = $(this).closest('.list_item').find('.list_title').text();
        $('#create_task_popup').show();
        // Збереження посилання на поточний елемент
        var $currentListItem = $(this).closest('.list_item');
        // Збереження посилання на форму додавання завдання
        var $createTaskForm = $('#create_task_form');

        // Вішаємо подію submit на форму додавання завдання
        $createTaskForm.off('submit').submit(function(event) {
            event.preventDefault();
            var title = $('#task_title').val();
            var description = $('#task_description').val();
            var end_date = $('#task_end_date').val();

            // Форматування кінцевої дати у потрібний вигляд (рік-місяць-день)
            var end_date_formatted = new Date(end_date).toISOString().split('T')[0];

            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            $.ajax({
                type: 'POST',
                url: 'task_create/',
                headers: { "X-CSRFToken": csrftoken },
                data: {
                    'title': title,
                    'description': description,
                    'end_date': end_date_formatted,
                    'list_name': listName,
                },
                success: function(data) {
                    $('#create_task_popup').hide();
                    // Оновлення списку тасків
                    $currentListItem.find('.tasks').append('<div class="task_item"><div class="task_title">' + title + '</div><div class="task_description">' + description + '</div><div class="task_end_date">' + end_date_formatted + '</div></div>');
                }
            });
        });
    });   

    $(document).on('click', function(event) {
        if (!$(event.target).closest('#create_task_popup').length && !$(event.target).is('#create_task')) {
            $('#create_task_popup').hide();
        }
    });
});
