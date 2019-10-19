from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import users
import bcrypt

def index(request):
    return render(request, "log_reg_app/index.html")

def register(request):
    errors = users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
             messages.error(request, value)
        return redirect("/")
    if request.POST['password'] == request.POST['confirm_password']:
        new_user = users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], password=request.POST['password'], email=request.POST['email'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        return redirect ('/success')
    else:
        return redirect('/')
    
def auth(request):
    logged_user = users.objects.filter(email=request.POST['email'])
    print(logged_user)
    if logged_user[0]:
        if logged_user[0].password == request.POST['password']:
            request.session['user'] = logged_user[0].first_name
            request.session['id'] = logged_user[0].id
            return redirect('/success')
    else:
        return redirect('/')

def success(request):
    if 'user' not in request.session: 
        print('user not in session')
        return redirect ('/')

    return render(request,'log_reg_app/success.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def user(request, users_id):
    
    context = {
        'users' : users.objects.get(id=users_id)
    }
    return render(request,'log_reg_app/user.html', context)

def edit_user(request, users_id): 
    errors = users.objects.basic_validator(request.POST) 
    all_users = users.objects.all() 
    one_user = users.objects.get(id=users_id) 
    if one_user.email == request.POST['email']: 
        print("this is a valid email") 
    else: 
        for user in all_users: 
            if user.email == request.POST['email']: 
                messages.error(request, "Email has already been used") 
                return redirect('/user/' + request.session_id) 
    
    if len(errors) > 0: 
        for key, value in errors.items(): 
            messages.error(request, value) 
        return redirect ('/user/' + request.session_id) 
    else: 
        this_user = users.objects.get(id=users_id) 
        this_user.first_name = request.POST['first_name'] 
        this_user.last_name = request.POST['last_name'] 
        this_user.email = request.POST['email'] 
        this_user.password = request.POST['password'] 
        this_user.save() 
        return redirect('/quotes')