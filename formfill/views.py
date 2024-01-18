from django.shortcuts import render,HttpResponse,redirect
from .models import Form,Userform,UserformImage
# Create your views here.

def formfill (request):
    allform=Form.objects.all()
    context={'allform':allform,}

    return render(request,'formfill/formfill.html',context)

def formpost(request,slug):
    form=Form.objects.filter(slug=slug).first()
    context={'form':form}
    return render(request,'formfill/formpost.html',context)   

def userform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        guiders= request.POST.get('guiders')
        phone_no=request.POST.get('phone_no')
        city= request.POST.get('city')
        form_name= request.POST.get('form_name')
        

        # Handling file uploads
        photos = request.FILES.getlist('photos')

        user_form_instance = Userform.objects.create(name=name, guiders=guiders, phone_no=phone_no, city=city, form_name=form_name)

        for photo in photos:
             UserformImage.objects.create(userform=user_form_instance, photo=photo)
        
        # Userform.objects.create(name=name,guiders=guiders,phone_no=phone_no,city=city,form_name=form_name,photos=photos)



    
    return render(request,'formfill/userform.html')    