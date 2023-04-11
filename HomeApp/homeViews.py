from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def AddClass(request):
    return render(request, "AddClass.html")


def goToSetting(request):
    uid = request.session['uid']
    username = request.session['username']
    email = request.session['email']
    role = request.session['role']
    
    print(uid, username, email, role)
    
    
    
    context = {'username': username, 'email': email}
    return render(request, 'Setting.html', context)