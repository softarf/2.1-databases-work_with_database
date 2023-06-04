from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_param = request.GET.get("sort", "id")
    if sort_param != 'id':
        if sort_param == 'name':
            pass
        elif sort_param == 'max_price':
            sort_param = '-price'
        elif sort_param == 'min_price':
            sort_param = 'price'
        else:
            return HttpResponse(f"Неизвестный параметр сортировки: {sort_param}")
    template = 'catalog.html'
    products = Phone.objects.order_by(sort_param)
    context = {'phones': products}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = get_object_or_404(Phone, slug=slug)
    context = {'phone': product}
    return render(request, template, context)
