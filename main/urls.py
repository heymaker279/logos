from django.urls import path, re_path
from .views import *
# from ..api.views import RegisterAccount

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    # path('catalog/', CatalogView.as_view(), name="catalog"),
    path('about/', about, name="about"),
    # path('news/', news, name="news"),
    # path('cart/', cart, name="cart"),
    # path('login/', LoginAccount.as_view(), name="login"),
    # path('register/', RegisterAccount.as_view(), name="register"),
    # path('category/<slug:cat_slug>/', show_category, name="category"),
    path('category/<slug:cat_slug>/', CategoryListView.as_view(), name="category"),
    # path('category/<slug:cat_slug>/<slug:prod_slug>/', show_products, name="product"),
    path('category/<slug:cat_slug>/<slug:prod_slug>/', ProductDetailsView.as_view(), name="product"),

]
