from django.shortcuts import render
import pyrebase
# Create your views here.
from Profile import profileViews
from django.contrib.auth.decorators import login_required


config={
    "apiKey": "AIzaSyAq7-ziABaQCTxfeOlMIbv8jvfQk2B7lmQ",
    "authDomain": "pbl5-94125.firebaseapp.com",
    "databaseURL": "https://pbl5-94125-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "pbl5-94125",
    "storageBucket": "pbl5-94125.appspot.com",
    "messagingSenderId": "42461525472",
    "appId": "1:42461525472:web:e0519d8a1a0e0644f1e785",
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
storage = firebase.storage()



def postCancel(request):

    role = request.session['role']
    print(role)
    if(role == 'teacher'):
        return render(request, "Home.html")
    else:
        profileViews.profile(request)


def postUpdate(request):
    userId = request.session.get('uid')
    fullName = request.POST.get("fullName")
    phone = request.POST.get('phone')
    adress = request.POST.get('Adress')
    School = request.POST.get('School')
    url = request.POST.get('url')
    data ={"FullName":fullName,"Phone":phone,"Adress":adress,"School":School,"url":url}
    
 
    database.child("Users").child(userId).update(data)
    context = {'username': fullName}
    print("Update for userid: ", userId)
    return render(request,"Home.html", context)  
