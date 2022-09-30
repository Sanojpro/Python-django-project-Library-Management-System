#Project Library Management System
#---SANOJ KUMAR PRADHAN---#



from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from lms.models import Book


#Home function renders the home.html and show it to the client when called upon.
def Home(request):

    return render(request, "home.html")

#LoginUser function takes GET and POST request and serves the client accordingly.
def loginUser(request):

    if request.method=="POST":
        email= request.POST.get("email")
        password= request.POST.get("password")
        ad=User.objects.all()
        for i in ad:
            x=i.email
            if email==x:
                user= authenticate(username=i.username,password=password)

                if user is not None:
                    login(request, user)
            # A backend authenticated the credentials
                    return redirect("/admview")
                else:
                    messages.warning(request, 'Wrong credentials!')
                    return render(request, 'login.html')
        # No backend authenticated the credentials

    return render(request, 'login.html')



#This function takes a GET and POST request and serves the client accordingly.
def AdminSignup(request):

    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        exist= User.objects.all()
        email1=email.lower()
        for i in exist:
            if i.email==email1:
                messages.warning(request, 'Admin already registered!')
            else:
                user = User.objects.create_user(username=name,
                                        email=email1,
                                        password=password)
                user.save()
    return render(request, "signup.html")

#This function takes GET request, fetches data from the database and serves it to the client
def stuview(request):
    
        book=Book.objects.all()
        return render(request,"stuview.html",{'bk':book})

#This function takes a GET request,fetches the data from the database and serves it to the client.
def admview(request):

    if request.user.is_anonymous:
        return redirect("/login")
    else:
        book=Book.objects.all()
        return render(request, "admview.html",{'bk':book})

def logoutUser(request):
    logout(request)
    return render(request, 'login.html')



#This function takes POST request renders update.html and helps in assigning keys- to the instance "book" of the object Book.
#The instance is created using the primary key, which was fetched by splitting the URI.
def updatebutton(request):
    var = request.build_absolute_uri()
    id= (var.split("=")[1])
    book=Book.objects.get(pk=id)
    return render(request, "update.html",{'bk':book})

#This function takes POST request, takes input from the client and updates the book instance based on the data fetched from update function
def updatebook(request):

    if request.method=="POST":
        var1 = request.build_absolute_uri()
        id = (var1.split("=")[1])
        Bname=request.POST.get("name")
        Auth=request.POST.get("auth")
        Pub=request.POST.get("publisher")
        book=Book.objects.get(pk=id)

        book.NAME=Bname
        book.AUTHOR=Auth
        book.PUBLISHER=Pub

        book.save()
        return redirect("/admview")

#This function takes a POST request, takes the primary key after splitting the URI and helps in deleting the instance.
def deletebook(request):

    if request.method=="POST":
        var = request.build_absolute_uri()
        id = (var.split("=")[1])
        book = Book.objects.get(BID=id)
        book.delete()
    return redirect("/admview")

#This function takes a POST request,takes value from the client and adds the data into the database.
def addbook(request):

    if request.method=="POST":
        Bname=request.POST.get("name")
        Auth=request.POST.get("auth")
        Pub=request.POST.get("publisher")
        book=Book(NAME=Bname,AUTHOR=Auth,PUBLISHER=Pub)

        book.save()
    return redirect("/admview")

#This function takes GET request ,renders addbook.html and show it to the client when called upon.
def addbutton(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request, "addbook.html")


