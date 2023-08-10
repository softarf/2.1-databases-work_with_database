from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


ORDER = ''


def index(request):
    return redirect('catalog')


def show_catalog(request):
    global ORDER
    sort_param = request.GET.get("sort", "id")
    if sort_param != 'id':
        if sort_param == 'name':
            pass
        elif sort_param == 'min_price':
            sort_param = 'price'
        elif sort_param == 'max_price':
            sort_param = '-price'
        else:
            return HttpResponse(f"<p style='color: red'>Неизвестный параметр сортировки: {sort_param}</p>")
    ORDER = sort_param
    template = 'catalog.html'
    products = Phone.objects.order_by(sort_param)
    context = {'phones': products}
    return render(request, template, context)


def show_product(request, slug):
    global ORDER
    ORDER = 'min_price' if ORDER == 'price' else ('max_price' if ORDER == '-price' else ORDER)
    template = 'product.html'
    product = get_object_or_404(Phone, slug=slug)
    context = {'phone': product,
               'sorted': ORDER}
    return render(request, template, context)
