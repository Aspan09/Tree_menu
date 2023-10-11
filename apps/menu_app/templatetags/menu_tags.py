from django import template
from menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name).select_related('parent').order_by('parent_id', 'pk')
    request = context['request']
    current_path = request.path_info
    return {'menu_items': menu_items, 'current_path': current_path, 'request': request}
