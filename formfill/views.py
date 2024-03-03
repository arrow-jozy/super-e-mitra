from django.shortcuts import render,HttpResponse,redirect
from .models import Formfill,UserformImage
from django.contrib import messages
# Create your views here.



   

def formfill(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        guiders= request.POST.get('guiders')
        phone_no=request.POST.get('phone_no')
        city= request.POST.get('city')
        form_name= request.POST.get('form_name')
        

        # Handling file uploads
        photos = request.FILES.getlist('photos')

        user_form_instance = Formfill.objects.create(name=name, guiders=guiders, phone_no=phone_no, city=city, form_name=form_name)

        for photo in photos:
             UserformImage.objects.create(userform=user_form_instance, photo=photo)
        
        messages.success(request,'Your form has been submitted succesfully')
        # Userform.objects.create(name=name,guiders=guiders,phone_no=phone_no,city=city,form_name=form_name,photos=photos)



    
    return render(request,'formfill/userform.html')    