from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from django.contrib.auth import login, authenticate , logout
from account.models import Account
from account.forms import RegistrationForm , AccountAuthenticationForm
# Create your views here.

def home_view(request):
    context = {}
    return render(request, 'account/home.html', context)
    
def register_view(request):
    user = request.user
    if(user.is_authenticated):
        return HttpResponse(f"You are already authenticate as {user.email}.")
    context = {}

    if(request.POST):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if(destination):
                return redirect(destination)
            return redirect("home")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect("/home")


def login_view(request):
    context = {}

    user = request.user
    if(user.is_authenticated):
        return redirect("/home")
    
    destination = get_redirect_if_exists(request)

    if(request.POST):
        form = AccountAuthenticationForm(request.POST)
        if(form.is_valid()):
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if(user):
                login(request, user)
                if(destination):
                    return redirect(destination)
                return redirect("/home")
        else:
            context['login_form'] = form

    return render(request, "account/login.html", context)

def get_redirect_if_exists(request):
    redirecting = None
    if(request.GET):
        if(request.GET.get("next")):
            redirecting = str(request.GET.get("next"))
    return redirecting


def account_view(request, *args, **kwargs):
    context = {}
    user_id = kwargs.get("user_id")
    try:
        account = Account.objects.get(pk=user_id)
    except Account.DoesNotExist:
        return HttpResponse("That user doesn't exist.")

    if(account):
        context['id'] = account.id
        context['username'] = account.username
        context['email'] = account.email
        context['profile_image'] = account.profile_image.url
        context['hide_email'] = account.hide_email

        is_self = True
        is_friend = False
        user = request.user

        if(user.is_authenticated and user != account):
            is_self = False
        elif(not user.is_authenticated):
            is_self = False

        context['is_self'] = is_self
        context['is_friend'] = is_friend
        context['BASE_URL'] = '/' 

        return render(request, "account/account.html", context)

def account_search_view(request, *args, **kwargs):
    context = {}
    if(request.method == "GET"):
        search_query = request.GET.get("q")
        if(len(search_query) > 0):
            search_results = Account.objects.filter(email__icontains=search_query).filter(username__icontains=search_query).distinct()
            user = request.user
            accounts = []
            for account in search_results:
                print(account)
                accounts.append((account, False))
            context['accounts'] = accounts

    return render(request, "account/search_results.html", context)
