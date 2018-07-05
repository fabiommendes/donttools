from django.shortcuts import render, get_object_or_404, get_list_or_404


def index(request):
    """
    Página inicial.
    """
    return render(request, 'kanban/index.html', {})


def board(request, path):
    """
    Mostra um quadro Kanban completo com as colunas de To-do, Doing e Done.
    
    Oculta as issues escondidas.
    """
    ctx = {
        'board': board_from_path(path),
    }
    return render(request, 'kanban/board.html', ctx)


def done(request, path):
    """
    Mostra todas as issues Done.
    """
    ctx = {
        'board': board_from_path(path),
    }
    return render(request, 'kanban/done.html', ctx)


def backlog(request, path):
    """
    Mostra as issues do backlog (i.e., no estado To-do)
    """
    ctx = {
        'board': board_from_path(path),
    }
    return render(request, 'kanban/backlog.html', ctx)


def issue_detail(request, path, issue_id):
    """
    Mostra informações detalhadas da issue.
    """
    ctx = {
        'board': board_from_path(path),
    }
    return render(request, 'kanban/issue-detail.html', ctx)


def issue_edit(request, path, issue_id):
    """
    Edita issue.
    """
    ctx = {
        'board': board_from_path(path),
    }
    return render(request, 'kanban/issue-edit.html', ctx)


def board_from_path(path):
    return NotImplemented