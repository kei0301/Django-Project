from django.shortcuts import render, HttpResponse

def error(request):
    return render(request, 'error/error.html')