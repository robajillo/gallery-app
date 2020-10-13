from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.main, name='mainPage'), 
    path('search/', views.search_results, name='search'),
    path('images/<location>/',views.filter_by_location,name= 'filter_by_location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)