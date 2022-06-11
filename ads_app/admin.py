from django.urls import path
from django.shortcuts import render

from django import forms

from django.contrib import admin

# Register your models here.
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Ads, Category


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


# @admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'description', 'address', 'is_published']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Ads.objects.update_or_create(
                    name=fields[0],
                    balance=fields[1],
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/ads_app/ads/load_csv.html", data)


# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Category.objects.update_or_create(
                    name=fields[0],
                    balance=fields[1],
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/ads_app/category/csv_upload.html", data)


admin.site.register(Ads, AdsAdmin)
admin.site.register(Category, CategoryAdmin)
