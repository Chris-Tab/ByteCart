from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from django.contrib import messages
from django.urls import resolve, Resolver404

from .forms import AddressForm
from .models import Address
from billing.models import BillingProfile


def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    context = {"form": form}

    next_ = request.GET.get("next")
    next_post = request.POST.get("next")
    redirect_path = next_ or next_post

    if form.is_valid():
        instance = form.save(commit=False)
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

        if billing_profile is not None:
            instance.billing_profile = billing_profile
            address_type = request.POST.get("address_type", "shipping")
            instance.address_type = address_type
            instance.save()

            # Save address ID to session
            request.session[f"{address_type}_address_id"] = instance.id
            messages.success(request, "Address saved successfully")

            # Safe redirect to valid 'next' path or fallback
            if redirect_path:
                try:
                    resolve(redirect_path)  # check if it's resolvable
                    return redirect(redirect_path)
                except Resolver404:
                    pass

            return redirect("orders:process")

        messages.error(request, "Unable to save address - no billing profile")
        return redirect("orders:process")

    return render(request, "addresses/checkout/address_form.html", context)
