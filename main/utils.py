from .models import *
from django.db.models import Count

menu = [
    {'title': 'Главная', 'url_name': '/'},
    {'title': 'Каталог', 'url_name': '/catalog'},
    {'title': 'О нас', 'url_name': '/about'},
    {'title': 'Новости', 'url_name': '/news'},

]


class DataMixin:
    # paginate_by = 20

    def get_menu(self):
        context = {}
        context['menu'] = menu
        return context

    def get_user_context(self, **kwargs, ):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = None
            context['products'] = ProductInfo.objects.filter(is_published=True)
        else:
            products = ProductInfo.objects.filter(product__category__slug=context['cat_selected'], is_published=True)
            context['products'] = products
        return context
