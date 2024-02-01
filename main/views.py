# from asyncio import mixins
# from django.http import JsonResponse
# from django.core.validators import URLValidator
# from django.db import IntegrityError
# from django.db.models import Q, Sum, F
# from yaml import load as load_yaml, Loader
# import yaml
# from rest_framework import viewsets, mixins
from urllib import request
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView
import requests
from .serializers import *
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.urls import reverse_lazy
from.forms import *
# from .serializers import OrderSerializer
# from .utils import *
# from .models import *
from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, DetailView
# from django_filters.rest_framework import DjangoFilterBackend
# from requests import get
# from django.contrib.auth.forms import UserCreationForm

from .utils import DataMixin


def get_context_main_menu():
    context = {
        'title': "LogosMetall",
    }
    return context


# class LoginView(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#
#     def post(self, request):
#         pass
class BaseView(DataMixin, ListView):
    model = News
    template_name = 'main/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # def get_queryset(self):
    #     return News.objects.all()


class CatalogView(DataMixin, ListView):
    model = ProductInfo
    template_name = 'main/catalog.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Каталог')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return ProductInfo.objects.filter(is_published=True)


class CategoryListView(DataMixin, ListView):
    model = Category
    template_name = 'main/catalog.html'
    context_object_name = 'category'
    # slug_url_kwarg = 'cat_slug'
    allow_empty = False

    def get_queryset(self):
        return Category.objects.filter(slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['category'][0].name),
                                      cat_selected=context['category'][0].slug)
        context = dict(list(context.items()) + list(c_def.items()))
        context['parameter'] = ProductParameter.objects.filter(product_info__product__category__slug=self.kwargs['cat_slug'])


        # context['form_quantity'] = OrderItemCreateForm
        # context['form_parameter'] = ProductParameterForm

        return context


# def show_products(request, cat_slug, prod_slug):
#     product = ProductInfo.objects.filter(product__slug=prod_slug)
#     product_parameter = ProductParameter.objects.filter(product_info__product__slug=prod_slug)
#     context = {
#         'product': product,
#         'parameter': product_parameter
#     }
#
#     return render(request, 'main/product.html', context=context)


class ProductDetailsView(DataMixin, DetailView):
    model = ProductInfo
    template_name = 'main/product.html'
    context_object_name = 'product'
    self_url_kwarg = ('prod_slug', 'cat_slug')
    allow_empty = False

    def get_object(self, queryset=None):
        product = ProductInfo.objects.filter(product__slug=self.kwargs['prod_slug'])
        # print(product)
        return product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['parameter'] = get_parameter(prod_slug=self.kwargs['prod_slug'])
        context['parameter'] = ProductParameter.objects.filter(product_info__product__slug=self.kwargs['prod_slug'])
        # context['quantity'] = OrderItemCreateForm()
        context['category'] = Category.objects.filter(slug=self.kwargs['cat_slug'])
        # context['parameter'] =
        c_def = self.get_user_context(cat_selected=context['category'][0].slug)
        context = dict(list(context.items()) + list(c_def.items()))
        return context


def about(request):
    news = News.objects.all()
    context = get_context_main_menu()
    context['news'] = news
    return render(request, 'main/about.html', context=context)


# class RegisterAccount(DataMixin, APIView):
#     """
#     Класс для регистрации покупателей
#     """
#
#     success_url = reverse_lazy('login')
#
#     def get(self, request, *, object_list=None, **kwargs):
#         context = super().get_user_context(**kwargs)
#         c_def = self.get_menu()
#         context = dict(list(context.items()) + list(c_def.items()))
#
#         context['reg_form'] = UserCreationForm()
#
#         return render(request, 'main/register.html', context)
#
#     def post(self, request):
#         """
#         Регистрация нового пользователя
#         \n:param request: запрос пользователя с обязательными параметрами в теле запроса
#         \n:return: добавляет нового пользователя и/или возвращает статус ответа
#         """
#         if {'first_name', 'last_name', 'email', 'password'}.issubset(
#                 request.data):  # проверяем обязательные аргументы
#             try:
#                 validate_password(request.data['password'])
#             except Exception as password_error:
#                 error_array = []
#                 for item in password_error:
#                     error_array.append(item)
#                 return JsonResponse({'Status': False, 'Errors': {'password': error_array}})
#             else:
#                 request.data.update({})
#                 user_serializer = UserSerializer(data=request.data)  # сохраняем пользователя
#                 if user_serializer.is_valid():
#                     user = user_serializer.save()
#                     user.set_password(request.data['password'])
#                     user.save()
#                     # new_user_register_send_message.delay(user_id=user.id)
#                     # return JsonResponse({'Status': True})
#                     return render(request, 'main/index.html')
#                 else:
#                     return JsonResponse({'Status': False, 'Errors': user_serializer.errors})
#         resp = JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})
#         return resp
        # return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


# def login(request):
#     return render(request, 'main/login.html', context=get_context_main_menu())


# class LoginAccount(DataMixin, APIView):
#     """
#     Класс для авторизации пользователей
#     """
#
#     def get(self, request, *, object_list=None, **kwargs):
#         context = super().get_user_context(**kwargs)
#         c_def = self.get_menu()
#         context = dict(list(context.items()) + list(c_def.items()))
#
#         context['log_form'] = LoginForm()
#
#         return render(request, 'main/login.html', context)
#
#     def post(self, request):
#         """
#         Авторизация пользователя методом POST
#         \n:param request: запрос пользователя с email и password в теле запроса
#         \n:return: возвращает токен пользователя и/или статус ответа
#         """
#         if {'email', 'password'}.issubset(request.data):
#             user = authenticate(request, username=request.data['email'], password=request.data['password'])
#             if user is not None:
#                 if user.is_active:
#                     token, _ = Token.objects.get_or_create(user=user)
#                     return JsonResponse({'Status': True, 'Token': token.key})
#             return JsonResponse({'Status': False, 'Errors': 'Не удалось авторизовать'})
#         return JsonResponse({'Status': False, 'Errors': 'All necessary arguments are not specified'})

# class PartnerStateViewSet(mixins.ListModelMixin,
#                           mixins.CreateModelMixin,
#                           viewsets.GenericViewSet):
#     """
#     Класс для работы со статусом поставщика
#     """
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer
#     permission_classes = [IsAuthenticated, IsOwner]
#
#     def list(self, request, *args, **kwargs):
#         """
#         Получение текущего статуса магазина
#         \n:param request: запрос пользователя
#         \n:return: возвращает id магазина, название, статус магазина (принимает или не принимает заказы)
#         """
#         # shop = request.user.shop
#         # serializer = ShopSerializer(shop)
#         return Response(serializer.data)
#
#     def create(self, request, *args, **kwargs):
#         """
#         Изменение текущего статуса магазина
#         \n:param request: запрос пользователя со статусом формата - {"state":<bool>} где bool = 0 или 1
#         \n:return: меняет статус магазина и возвращает статус ответа
#         """
#         state = request.data.get('state')
#         if state:
#             try:
#                 # Shop.objects.filter(user_id=request.user.id).update(state=strtobool(state))
#                 # return JsonResponse({'Status': True})
#             except ValueError as error:
#                 return JsonResponse({'Status': False, 'Errors': str(error)})
#
#         return JsonResponse({'Status': False, 'Errors': 'All necessary arguments are not specified'})
#
# class PartnerOrdersViewSet(mixins.ListModelMixin,
#                            viewsets.GenericViewSet):
#     """
#     Класс для получения заказов поставщиками
#     """
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated, IsOwner, IsShop]
#
#     def list(self, request, *args, **kwargs):
#         """
#         Получение списка заказов магазином
#         \n:param request: запрос пользователя
#         \n:return: возвращает id заказа, список товаров, статус заказа, дату формирования,
#         общую сумму заказа и контактные данные покупателя
#         """
#         try:
#             order = Order.objects.filter(
#                 ordered_items__product_info__shop__user_id=request.user.id).exclude(
#                 state='basket').prefetch_related(
#                 'ordered_items__product_info__product__category',
#                 'ordered_items__product_info__product_parameter__parameter').select_related('contact').annotate(
#                 total_sum=Sum(F('ordered_items__quantity') *
#                               F('ordered_items__product_info__price'))).distinct()  # структурирование информации
#             serializer = OrderSerializer(order, many=True)
#             return Response(serializer.data)
#         except ValueError as error:
#             return JsonResponse({'Status': False, 'Error': error})
#
# class PartnerUpdate(APIView):
#     """
#     Класс для обновления прайса от поставщика
#     """
#
#     def post(self, request, *args, **kwargs):
#         """
#         Добавление и обновление информации от поставщика
#         \n:param request: запрос пользователя с указанием минимум одного из двух параметров в теле запроса
#         в которых нужно указать путь к данным формата yaml
#         пример -
#         {'url': 'https://path_to_file.yaml'} путь к url с данными
#         {'file': 'data/data.yaml'} относительный или абсолютный путь к yaml файлу
#         \n:return: добавляет информацию в базу данных и возвращает статус ответа
#         """
#         if not request.user.is_authenticated:
#             return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)
#         if request.user.type != 'shop':  # проверка на тип пользователя (магазин)
#             return JsonResponse({'Status': False, 'Error': 'Only for shop'}, status=403)
#         try:
#             user_id = request.user.id
#             filename = request.data.get('file')
#             url = request.data.get('url')
#             if filename:  # извлечение информации из файла
#                 with open(filename, 'r', encoding='utf-8') as stream:
#                     data = yaml.safe_load(stream)
#             elif url and filename is None:  # извлечение информации с url
#                 validate_url = URLValidator()
#                 validate_url(url)
#                 stream = get(url).content
#                 data = load_yaml(stream, Loader=Loader)
#             else:
#                 JsonResponse({'Status': False, 'Error': 'The source of information is incorrectly specified'})
#             try:  # загрузка информации в базу данных
#                 # shop, _ = Shop.objects.get_or_create(name=data['shop'], user_id=user_id)
#             except IntegrityError as error:
#                 return JsonResponse({'Status': False, 'Error': f'{error}'})
#             # Shop.objects.filter(user_id=user_id).update(filename=filename, url=url)
#             for category in data['categories']:
#                 category_object, _ = Category.objects.get_or_create(id=category['id'], name=category['name'])
#                 # category_object.shops.add(shop.id)
#                 category_object.save()
#             # ProductInfo.objects.filter(shop_id=shop.id).delete()
#             for item in data['goods']:
#                 product, _ = Product.objects.get_or_create(name=item['name'], category_id=item['category'],
#                                                            id=item['id'])
#                 product_info = ProductInfo.objects.create(product_id=product.id,
#                                                           model=item['model'],
#                                                           price=item['price'],
#                                                           price_rrc=item['price_rrc'],
#                                                           quantity=item['quantity'],
#                                                           # shop_id=shop.id
#                                                           )
#                 for name, value in item['parameters'].items():
#                     parameter_object, _ = Parameter.objects.get_or_create(name=name)
#                     ProductParameter.objects.create(product_info_id=product_info.id,
#                                                     parameter_id=parameter_object.id,
#                                                     value=value)
#             return JsonResponse({'Status': True})
#         except BaseException as error:
#             return JsonResponse({"Status": "False", "Error": f"{error.__str__()}"})
