from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages 


def index(request):
    
    context ={
    'all_quotes' : quotes.objects.all(),
    'user' : users.objects.get(id=request.session['id'])
    
    }
    print(quotes.objects.all())
    return render(request,'quotes_app/quotes.html', context)

def add_quote(request):
    if request.method == "POST" : 
        print('in the if check')
        errors = quotes.objects.basic_validator(request.POST)
        if len(errors) > 0:
            print("data was no good")
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/quotes')
        else:
            print('record has been created')
            new_quote = quotes.objects.create(author=request.POST['author'], quote=request.POST['quote'],posted_by=users.objects.get(id=request.session['id']))
            user = users.objects.get(id=request.session['id'])
            new_quote.users_who_like.add(user) 
    return redirect('/quotes')

def view_poster(request, quotes_id):

    this_poster = users.objects.get(id=quotes_id)
    
    context = {
        'this_poster' : this_poster,
    }

    return render(request,'quotes_app/poster.html', context)

def like_quote(request, quotes_id):
    this_quote = quotes.objects.get(id=quotes_id)
    this_user = users.objects.get(id=request.session['id'])
    this_quote.users_who_like.add(this_user)
    return redirect('/quotes')

def delete_quote(request, quotes_id):
    
    one_book = quotes.objects.get(id=quotes_id)
    one_book.delete()

    return redirect('/quotes')
