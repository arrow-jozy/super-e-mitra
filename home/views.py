from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login 



# Create your views here.
def home(request):
    popular_blog=Post.objects.filter(blogtype='popular')
    context={'popular_blog':popular_blog}

    return render(request,'home/index.html',context)
def contact(request):
  
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        city=request.POST['city']
        content=request.POST['content']
        if len(name)<2 or len(city)<2 or len(phone)<9 or  len(content)<2 :
            messages.error(request,'please! fill the form correctly')
        else:
            messages.success(request,'Your form has been submitted succesfully')
        contact=Contact(name=name,phone=phone,city=city,content=content)
        contact.save()
    
    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')

def search(request):
    query=request.GET['query']
    if not query:
        allpost=[]
        
        

    else: 
        allpostTitle=Post.objects.filter(title__icontains=query)
        allpostContent=Post.objects.filter(content__icontains=query)
        allpost=allpostTitle.union(allpostContent) 
    params={'allpost':allpost,'query':query}
    return render(request,'home/search.html',params)

 
def signup(request):
    if request.method=='POST':
        #GET the parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
       
        # Checks for error input
        if len(username)> 10 or len(username) < 3:
            messages.error(request,"Username should be more than 3 or less then 10 characters")
            return redirect('home') 
        if not username.isalnum():
            messages.error(request,"Username should only contain alphabet and numbers")
            return redirect('home') 
        if pass1 != pass2 :
            messages.error(request,"Password do not match")
            return redirect('home') 

        #create user     

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been succesfully created")
        return redirect('home')

    else:
        return HttpResponse("404:Not found")

def handle_login (request):
   if request.method=="POST":
      
      loginusername=request.POST['loginusername']        
      loginpassword=request.POST['loginpassword']

      user=authenticate(username=loginusername,password=loginpassword) 
      if user is not None:
          login(request,user)
          messages.success(request,"Log in succesfull") 
          return redirect('home')
      else:
          messages.error(request,"invalid username or password")  
          return redirect('home')    


def handle_logout(request):
    
    logout(request)
    messages.success(request,"Logout succesfull") 
    return redirect ('home')

def waiting(request):
    return render(request,'home/waiting.html')