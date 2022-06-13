from django.shortcuts import render, HttpResponse

def account(request):
    return render(request, 'account/account.html')

def thread(request):
    return render(request, 'account/account_thread.html')

def register(request):
    return render(request, 'account/account_register.html')

def login(request):
    return render(request, 'account/account_login.html')

def reset(request):
    return render(request, 'account/account_reset.html')

def change(request):
    return render(request, 'account/account_change.html')

def thanks(request):
    return render(request, 'account/account_register_thanks.html')

def settings(request):
    return render(request, 'account/account_settings.html')

def update(request):
    return render(request, 'account/account_update.html')

def invite(request):
    return render(request, 'account/account_invite.html')