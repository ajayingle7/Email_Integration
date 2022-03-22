from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def laptopView(request):
    template_name = "app1/laptopview.html"
    form = LaptopForm()
    context = {"form":form}

    if request.method=="POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()



    return render(request,template_name,context)


@login_required()
def laptopData(request):
    template_name = "app1/laptopdata.html"
    data = Laptop.objects.all()
    context = {"data":data}


    return render(request,template_name,context)



def updateView(request,id):
    template_name = "app1/laptopview.html"
    obj = Laptop.objects.get(id=id)
    form = LaptopForm(instance=obj)
    context = {"form":form}

    if request.method=="POST":
        form = LaptopForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()

            return redirect("laptopdata")


    return render(request,template_name,context)




def deleteView(request,id):
    template_name = "app1/confirm.html"
    obj = Laptop.objects.get(id=id)
    context = {"data":obj}
    if request.method=="POST":
        obj.delete()

        return redirect("laptopdata")





    return render(request,template_name,context)





def errorView(request,exception):
    template_name = "app1/errors.html"
    context  ={}


    return render(request,template_name,context)









