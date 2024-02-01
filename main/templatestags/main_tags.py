from django import template
from ..models import *


register = template.Library()


# @register.simple_tag()
# def get_products():
#     return Product.objects.all()


@register.simple_tag(name='get_cats')
def get_categories():
    return Category.objects.all()


'''  Тег простой

'''


@register.simple_tag(name='getmenu')
def get_menu(filter=None):
    menu = [{'title': 'О нас', 'url_name': 'about'},
            {'title': 'Новости', 'url_name': 'news'},
            {'title': 'Корзина', 'url_name': 'cart'},
            # {'title': 'Войти', 'url_name': 'login'},
    ]
    return menu

#
#
#
# '''
#     Включающий тег
# '''


@register.inclusion_tag('main/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}