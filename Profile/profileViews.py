from django.shortcuts import render
import pyrebase
# Create your views here.


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

def profile(request):
    return render(request, "Profiles.html")


def goToSettingViews(request):
    return render(request, )


