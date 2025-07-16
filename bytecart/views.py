from django.shortcuts import render
from .forms import ContactForm


def home_page(request): 
    context = {}
    if request.user.is_authenticated:
        context["premium_content"] = (
            "Welcome back! You have access to your library, order history, and exclusive content."
        )
    return render(request, "bytecart/home_page.html", context)


def about_page(request):
    # Currently not used in project — can be removed if not planned
    context = {
        "title": "About ByteCart",
        "content": "ByteCart is your go-to platform for curated digital content and eBooks."
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form": contact_form,
        "title": "Contact Us",
        "content": "We’d love to hear from you! Send us your feedback or questions using the form below."
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        # Future: send email or save to DB
    return render(request, "contact/view.html", context)


def privacy_policy_page(request):
    return render(request, "base/privacy.html")


def terms_page(request):
    return render(request, "base/terms.html")
