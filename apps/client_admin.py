from django.contrib.admin import AdminSite
from django.contrib import admin

from apps.forms import CustomAuthForm
from apps.models import Category, Product


class ClientAdminSite(AdminSite):
    site_header = "Client uchun adminka"
    site_title = "Client Events Admin Portal"
    index_title = "Welcome to Client Researcher Events Portal"
    login_form = CustomAuthForm
    login_template = 'admin/custom/custom_login.html'


client_admin_site = ClientAdminSite(name='client_admin')


@admin.register(Product, Category, site=client_admin_site)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = 'name', 'id'
