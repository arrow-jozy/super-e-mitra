from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login 


#selenium import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
# Create your views here.
def home(request):
 

    return render(request,'home/index.html')
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

def automate(request):
       if request.method=='POST':
            service_obj=Service("D:\driver\chromedriver.exe")
            driver=webdriver.Chrome(service=service_obj)
            driver.get("https://irgyurban.rajasthan.gov.in/Home/JobCardDetails")
            driver.maximize_window()
            year=Select(driver.find_element(By.XPATH,"//*[@id='fyYear']"))
            year.select_by_visible_text('2023')
            jobcard_no=driver.find_element(By.ID,'jobcard').send_keys("JC202261020000045574")
            driver.find_element(By.XPATH,"//*[@id='content-wrapper']/div[2]/div[1]/div/div/div[5]/button").click()
            time.sleep(5)
            messages.success(request,'Thanks for using our script')           

       return render(request,'home/automate.html')