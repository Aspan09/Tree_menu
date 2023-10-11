from django.shortcuts import render
from .models import MenuItem


def draw_menu(request, menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name).select_related('parent').order_by('parent_id', 'pk')
    current_path = request.path_info
    return render(request, 'menu.html', {'menu_items': menu_items, 'current_path': current_path, 'request': request})
