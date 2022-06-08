from django.contrib import admin

# Register your models here.
from ads_app.models import Ads, Category


class AdsAdmin(admin.ModelAdmin):
    list_ads = ('name', 'author', 'price', 'description', 'address', 'is_published')

    # def get_urls(self):
    #     urls = super().get_urls()
    #     new_urls = [path('', self.)]


# class CategoryAdmin(admin.ModelAdmin):
#     list_category = ('name')


admin.site.register(Ads)
admin.site.register(Category)
