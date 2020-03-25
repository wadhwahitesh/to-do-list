from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="Base"),
    path("home/", views.home, name="home"),
    path("<int:id>", views.displaylist, name="List"),
    path("create/", views.create, name="create"),
    path("lists/",views.lists,name="lists"),
    path('delete/', views.deleteList, name="deleteList"),
    path('delete<int:id>/', views.deleteItem, name="deleteItem"),

]
