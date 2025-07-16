from django.shortcuts import render, redirect
from accounts.forms import LoginForm, GuestForm
from orders.models import Order
from products.models import Product
from .models import Cart
from billing.models import BillingProfile
from accounts.models import GuestEmail
from addresses.forms import AddressForm



def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/cart_home.html', {"cart": cart_obj})


def cart_update(request):
    product_id = request.POST.get("product_id")
    if product_id:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Product not found!")
            return redirect("carts:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)

        request.session["cart_items"] = cart_obj.products.count()
    else:
        print("No product_id provided in POST data.")
    return redirect("carts:home")




def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    if cart_created or cart_obj.products.count() == 0:
        return redirect("carts:home")

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_form = AddressForm()

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

    if billing_profile is None:
        return render(request, "carts/checkout_home.html", {
            "billing_profile": None,
            "login_form": login_form,
            "guest_form": guest_form,
        })

    order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)

    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form,
        "address_form": address_form,
        "billing_address_form": billing_address_form,
    }

    return render(request, 'carts/checkout_home.html', context)