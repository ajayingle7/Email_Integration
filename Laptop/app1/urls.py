from django.urls import path
from .views import laptopView,laptopData,updateView,deleteView



urlpatterns = [


    path("laptop/", laptopView, name= "laptopview"),
    path("laptopdata/", laptopData, name="laptopdata" ),
    path("update/<int:id>/", updateView, name="update" ),
    path("delete/<int:id>/", deleteView, name="delete")


]