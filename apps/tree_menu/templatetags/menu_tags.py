from django import template
from django.urls import resolve
from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        current_url = resolve(context['request'].path_info).url_name

        def build_tree(parent=None):
            items = menu.items.filter(parent=parent).select_related('parent')
            tree = []
            for item in items:
                tree.append({
                    'item': item,
                    'children': build_tree(parent=item),
                    'active': item.get_url() == context['request'].path
                })
            return tree

        menu_tree = build_tree()
        return {'menu_tree': menu_tree, 'current_url': current_url}
    except Menu.DoesNotExist:
        return {'menu_tree': [], 'current_url': ''}

