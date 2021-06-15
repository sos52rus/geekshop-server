from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from products.models import Product
from basket.models import Basket


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, id):
    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete_position(request, product_id):
    basket = Basket.objects.get(product=product_id)

    if basket.quantity == 1:
        Basket.objects.get(product=product_id).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket.quantity -= 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
