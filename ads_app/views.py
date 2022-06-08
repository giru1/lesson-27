import csv
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from sqlalchemy.dialects.mssql.information_schema import views

from ads_app.models import Ads, Category


def index(request):
    return JsonResponse({
        "status": "ok"
    })


@method_decorator(csrf_exempt, name='dispatch')
class LoadCSV(View):
    def get(self, request):
        return JsonResponse({
            "status": "ok"
        })

    def post(self, request):
        with open('datasets/ads.csv', newline='', encoding='utf-8') as File:
            reader = csv.reader(File)
            print(type(reader))
            count = 0
            for row in reader:
                count += 1
                if count > 1:
                    # ads = Ads.objects.create(
                    #     name=row["name"],
                    #     author=row["author"],
                    #     price=row["price"],
                    #     description=row["description"],
                    #     address=row["address"],
                    #     is_published=row["is_published"],
                    # )
                    print(row[1])
        return JsonResponse({
            "status": "ok"
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        ads = Ads.objects.all()

        response = []
        for ad in ads:
            response.append({
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)

        ads = Ads.objects.create(
            name=data["name"],
            author=data["author"],
            price=data["price"],
            description=data["description"],
            address=data["address"],
            is_published=data["is_published"],
        )

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request):
        category = Category.objects.all()

        response = []
        for cat in category:
            response.append({
                'id': cat.id,
                'name': cat.name,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)

        category = Category.objects.create(
            name=data['name'],
        )
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name,
        })
