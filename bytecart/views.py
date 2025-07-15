from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title": "Hello World",
        "content": "Welcome to the ByteCart home page!",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEAH! You are logged in."
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "About Page",
        "content": "This is the about page of ByteCart, where you can learn more about us.",
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page",
        "content": "Feel free to reach out to us through the contact page.",
        "form": contact_form,     
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)        
    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form        
    }   
    print('User is authenticated:')
    # print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        # print(request.user.is_authenticated)
        if user is not None:
            # print(request.user.is_authenticated)
            login(request, user)
            context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Invalid credentials") 

    return render(request, "auth/login.html", context )

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form        
    }       
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)

def home_page_old(request):
    html_ = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">
  </head>
  <body>
    <div class="text-center">
    <h1>Hello, world!</h1>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js" integrity="sha384-ndDqU0Gzau9qJ1lfW4pNLlhNTkCfHzAVBReH9diLvGRem5+R9g2FzA8ZGN954O5Q" crossorigin="anonymous"></script>
  </body>
</html>
    """
    return HttpResponse(html_)