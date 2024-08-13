from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from catalog.models import Product

@login_required
def create_order(request):
    if request.method == 'POST':
        # Получите выбранные товары из формы
        product_ids = request.POST.getlist('products')
        products = Product.objects.filter(id__in=product_ids)
        order = Order.objects.create(user=request.user)
        order.products.set(products)
        order.save()
        return redirect('orders:order_success')
    else:
        products = Product.objects.all()
    return render(request, 'orders/create_order.html', {'products': products})

def order_success(request):
    return render(request, 'orders/order_success.html')

