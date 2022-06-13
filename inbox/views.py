from django.shortcuts import render, HttpResponse

def inbox(request):
    return render(request, 'inbox/inbox.html')