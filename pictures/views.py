from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import Category, Location, Image




def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_category})

    else:
        message = "You didn't search for any category"
        return render(request, 'search.html',{"message":message})
    
def main(request):
    try:        
        images = Image.objects.all()
        category = Category.objects.all()
        location = Location.objects.all()
    except DoesNotExist:
        raise Http404()
    return render(request,'index.html',{'images':images, 'category':category, 'location':location})

def filter_by_location(request,location):
  image= Image.filter_by_location(location)
  
  
  return render(request,'location.html',{'images':image})
  