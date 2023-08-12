from django.shortcuts import render

# Create your views here.

def idx(request):
    return render(request, './index.html') 