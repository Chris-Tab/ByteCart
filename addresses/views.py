from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import AddressForm
from billing.models import BillingProfile

def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    context = {"form": form}

    next_ = request.GET.get("next")
    next_post = request.POST.get("next")
    redirect_path = next_ or next_post or None

    if form.is_valid():
        instance = form.save(commit=False)
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

        if billing_profile is not None:
            instance.billing_profile = billing_profile
            instance.address_type = request.POST.get("address_type", "shipping")
            instance.save()
        else:
            return redirect("checkout")  # ✅ simplified

        if url_has_allowed_host_and_scheme(redirect_path, allowed_hosts={request.get_host()}):
            return redirect(redirect_path)
        else:
            return redirect("checkout")  # ✅ corrected fallback

    return redirect("checkout")  # ✅ fallback in case of invalid form
