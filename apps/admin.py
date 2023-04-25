# from django.contrib import admin
# from django.contrib.admin.sites import DefaultAdminSite
# from django.db.models import Count
# from django.forms import forms
# from django.http import HttpResponse
# from django.shortcuts import redirect, render
# from django.urls import path
# from django.utils.safestring import mark_safe
# import csv
# import io

# from apps.models import Category, Product, Tag, Origin, Hero, Villain
#
#
# class ExportCsvMixin:
#     def export_as_csv(self, request, queryset):
#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields]
#
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
#         writer = csv.writer(response)
#
#         writer.writerow(field_names)
#         for obj in queryset:
#             row = writer.writerow([getattr(obj, field) for field in field_names])
#
#         return response
#
#     export_as_csv.short_description = "Export Selected"
#
#
# class CsvImportForm(forms.Form):
#     csv_file = forms.FileField()
#
#
# # @admin.register(Tag)
# # class TagModelAdmin(admin.ModelAdmin, ExportCsvMixin):
# #     actions = ['export_as_csv']
# #     change_list_template = "apps/tags_changelist.html"
# #
# #     def get_urls(self):
# #         urls = super().get_urls()
# #         my_urls = [
# #             path('import-csv/', self.import_csv),
# #         ]
# #         return my_urls + urls
# #
# #     def import_csv(self, request):
# #         if request.method == "POST":
# #             csv_file = request.FILES["csv_file"]
# #             decoded_file = csv_file.read().decode('utf-8')
# #             io_string = io.StringIO(decoded_file)
# #             bulk = []
# #             for row in csv.DictReader(io_string):
# #                 row.pop('id')
# #                 bulk.append(Tag(**row))
# #                 # Tag.objects.update_or_create(row, id=row['id'])
# #                 # Tag.objects.create(id=row["id"], name=row["name"])
# #             Tag.objects.bulk_create(bulk)
# #             self.message_user(request, "Your csv file has been imported")
# #             return redirect("..")
# #         form = CsvImportForm()
# #         context = {
# #             "form": form
# #         }
# #         return render(request, 'apps/csv_form.html', context)
#
#
# @admin.register(Product)
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
# #
# # class ProductStackedInline(admin.StackedInline):
# #     model = Product
# #     min_num = 0
# #     extra = 2
# #     max_num = 4
# #     can_delete = False
# #
# #     # readonly_fields = ['name']
# #
# #
# # @admin.register(Category)
# # class CategoryModelAdmin(admin.ModelAdmin):
# #     list_display = 'name', 'id'
# #     change_list_template = 'admin/custom/change_list.html'
# #     inlines = (ProductStackedInline,)
# #
# #
# # # admin.register(Product, ProductModelAdmin)
# #
# #
# # @admin.register(Hero)
# # class HeroModelAdmin(admin.ModelAdmin):
# #     pass
# #     # list_display = ("name", "hero_count", "villain_count")
# #
# #
# # @admin.register(Origin)
# # class OriginAdmin(admin.ModelAdmin):
# #     list_display = ('name', 'hero_count', 'villain_count')
# #
# #     def get_queryset(self, request):
# #         queryset = super().get_queryset(request)
# #         queryset = queryset.annotate(
# #             _hero_count=Count("hero", distinct=True),
# #             _villain_count=Count("villain", distinct=True),
# #         ).order_by('_hero_count', '_villain_count')
# #         return queryset
# #
# #     def hero_count(self, obj):
# #         return obj._hero_count
# #
# #     def villain_count(self, obj):
# #         return obj._villain_count
# #
# @admin.register(Category)
# class CategoryModelAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Hero)
# class HeroModelAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Villain)
# class VillainModelAdmin(admin.ModelAdmin):
#     pass
#
# @admin.register(Origin)
# class OriginModelAdmin(admin.ModelAdmin):
#     pass
