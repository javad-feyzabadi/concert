from django.urls import path
from . import views
#from . views import ConsertCreateView
urlpatterns =[
    path('',views.ConsertListView,name='consert_list'),
    path('location/',views.LocationListView,name='location_list'),
    path('detail/<int:id>',views.DetailListView,name='detail_list'),
    path('time/',views.TimeListView,name='time_list'),
    path('edit/<int:id>',views.conserteditview,name='edit'),
    path('create/',views.ConsertCreateView,name='create'),
    path('delete/<int:id>',views.DeleteView,name='delete'),

    #path('create/',views.ConsertCreateView.as_view(),name='create'),



]
