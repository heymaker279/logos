from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import BaseInlineFormSet
from .models import *


class ProductParameterInline(admin.TabularInline):
    model = ProductParameter


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'position')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_editable = ['image', 'link', 'title']
    list_display = ['id', 'title', 'description', 'text', 'created_at', 'updated_at', 'link', 'image']


@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'text', 'created_at', 'updated_at', 'is_active', 'image']
    list_editable = ['title', 'description', 'text', 'is_active', 'image']


# @admin.register(Shop)
# class ShopAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'image')
    list_editable = ['slug', 'image']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'is_published')
    list_filter = ('product',)
    list_editable = ['is_published']
    inlines = [ProductParameterInline]


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ['name']


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_info', 'parameter', 'value', 'price')
    list_editable = ['product_info', 'parameter', 'value', 'price']


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'dt', 'state', )


# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     extra = 3


# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('id', 'order', 'product_info', 'quantity')
#     list_filter = ('product_info', )
#     search_fields = ['id', 'order']
    # inlines = [OrderItemInline, ]
    # #
    # def model(self, obj):
    #     return obj.ordered_items.get('model')

        # if obj.product_info.get('model'):
        #     model = obj.product_info.get('model')
        #     print(model)
            # return model
    # model.short_description = u'Размер'


# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'apt', 'building', 'street', 'city', 'house', 'phone')
#
#
# @admin.register(ConfirmEmailToken)
# class ConfirmEmailTokenAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'created_at', 'key')