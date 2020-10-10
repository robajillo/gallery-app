from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import Category, Location, Image

def main(request):
    return render(request,'index.html')


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_category})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})
    
