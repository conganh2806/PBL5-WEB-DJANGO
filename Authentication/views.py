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

def loginSignUp(request):
    return render(request, "Login.html")

def postSignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('password')
    name = request.POST.get('username')
    role = request.POST.get('roles')
    print(role)
    print(name)
    try:
        
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        print("signed up !")
        database.child("Users").child(user['localId']).set({"email": email, "username": name, "role": role})

    except:
        print("Sign up failed, account exist")
        return render(request, "Login.html")
    return render(request,"Login.html")



def postSignIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = authe.sign_in_with_email_and_password(email, password)
            userId = user['localId']
            request.session['uid'] = userId
            username = database.child('Users').child(userId).child('username').get().val()
            role = database.child('Users').child(userId).child('role').get().val()
            request.session['username'] = username
            request.session['email'] = email
            request.session['role'] = role
            context = {'username': username, 'email': email}
            print('Logged in!')
            # Nếu xác thực thành công, chuyển hướng đến trang chính
            if role=='teacher':
                return render(request, 'Home.html', context)
            else:
                return render(request, 'Profiles.html', context)
                
            
        except:
            # Nếu xác thực thất bại, trả về thông báo lỗi
            message = "Invalid email or password"
            return render(request, 'Login.html', {'message': message})
    else:
        return render(request, 'Login.html')
    

def logOut(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")





