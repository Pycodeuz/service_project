# from django.contrib.admin import AdminSite
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User, Group
# from django.db.models import Count
# from django.template.response import TemplateResponse
# from django.utils.safestring import mark_safe
#
# from apps.forms import CustomAuthForm
# from apps.models import Category, Product, Origin, Hero, Tag
#
#
# class ClientAdminSite(AdminSite):
#     site_header = "Client uchun adminka"
#     site_title = "Client Events Admin Portal"
#     index_title = "Welcome to Client Researcher Events Portal"
#     login_form = CustomAuthForm
#     login_template = 'admin/custom/custom_login.html'
#
#     def get_app_list(self, request, app_label=None):
#         """
#         Return a sorted list of all the installed apps that have been
#         registered in this site.
#         """
#
#         ordering = {
#             "Categories": 0,
#             'Heroes': 1,
#             "Products": 2,
#             "Entitys": 3,
#             "Origins": 4,
#             "Tags": 6,
#             "Groups": 1,
#             "Users": 2,
#         }
#         app_dict = self._build_app_dict(request)
#         # a.sort(key=lambda x: b.index(x[0]))
#         # Sort the apps alphabetically.
#         app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
#
#         # Sort the models alphabetically within each app.
#         for app in app_list:
#             app['models'].sort(key=lambda x: ordering[x['name']])
#
#         return app_list
#
#
# client_admin_site = ClientAdminSite(name='client_admin')
#
#
# # @admin.register(Product, Category, site=client_admin_site)
# # class CategoryProductAdmin(admin.ModelAdmin):
# #     list_display = 'name', 'id'
#
#
# @admin.register(Tag, site=client_admin_site)
# class TagModelAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(User, site=client_admin_site)
# class CustomUserAdmin(UserAdmin):
#     pass
#
#
# @admin.register(Product, site=client_admin_site)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = 'name', 'id'
#     date_hierarchy = 'created_at'
#     readonly_fields = ["botirjon"]
#
#     def botirjon(self, obj: Product):
#         head = obj.image
#         return mark_safe(f'<img src="{head.url}" width="200" height="200" />')
#
#
# class ProductStackedInline(admin.StackedInline):
#     model = Product
#     min_num = 0
#     extra = 2
#     max_num = 4
#     can_delete = False
#
#     # readonly_fields = ['name']
#
#
# @admin.register(Category, site=client_admin_site)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display = 'name', 'id'
#     change_list_template = 'admin/custom/change_list.html'
#     inlines = (ProductStackedInline,)
#
#
# # admin.register(Product, site=client_admin_site, ProductModelAdmin)
#
#
# @admin.register(Hero, site=client_admin_site)
# class HeroModelAdmin(admin.ModelAdmin):
#     pass
#     # list_display = ("name", "hero_count", "villain_count")
#
#
# @admin.register(Origin, site=client_admin_site)
# class OriginAdmin(admin.ModelAdmin):
#     list_display = ('name', 'hero_count', 'villain_count')
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         queryset = queryset.annotate(
#             _hero_count=Count("hero", distinct=True),
#             _villain_count=Count("villain", distinct=True),
#         ).order_by('_hero_count', '_villain_count')
#         return queryset
#
#     def hero_count(self, obj):
#         return obj._hero_count
#
#     def villain_count(self, obj):
#         return obj._villain_count
