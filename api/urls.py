from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from .views import RegisterAccount, LoginAccount, CategoryView, \
    BasketViewSet, \
    AccountDetailsViewSet, ConfirmAccount, \
    ProductInfoView, ContactView, OrderViewSet

r = DefaultRouter()
r.register('basket', BasketViewSet)
r.register('order', OrderViewSet)
r.register('user/details', AccountDetailsViewSet)

app_name = 'backend'
urlpatterns = [
    re_path(r'^user/contact', ContactView.as_view(), name='contact'),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    re_path(r'^user/login', LoginAccount.as_view(), name='user-login'),
    re_path(r'^user/password_reset', reset_password_request_token, name='password-reset'),
    re_path(r'^user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    re_path(r'^categories', CategoryView.as_view(), name='categories'),
    re_path(r'^products', ProductInfoView.as_view(), name='products'),
] + r.urls