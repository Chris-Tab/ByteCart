from django.shortcuts import render, redirect

from .models import Order

def order_process_view(request):
    if request.method == "POST":
        cart_id = request.session.get("cart_id")
        if cart_id:
            order_qs = Order.objects.filter(cart__id=cart_id)
            if order_qs.exists():
                order = order_qs.first()
                order.status = "paid"  # simulate payment
                order.save()
                return redirect("orders:success")  # You’ll create this page next
    return redirect("cart:home")

def order_success_view(request):
    return render(request, "orders/success.html")