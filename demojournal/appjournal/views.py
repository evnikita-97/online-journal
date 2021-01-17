from django.http import HttpResponse
from . models import User
from . models import Journal
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from . forms import SignUpForm
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

# Create your views here.


def details(request):
    u = User(id='', user_name='', mail_id='', password='', location='')
    u.save()
    e = Journal(id='', User_id='')
    e.save()
    return HttpResponse("Hi!")


def signup(request):
    if request.session.has_key('email'):
        print('My email is :' + request.session['email'])
        return redirect('/appjournal/profile')
    error_msg = ''
    if request.method == 'POST':
        print(request.POST)
        u_name = request.POST.get('name')
        password = request.POST.get('password')
        mail_id = request.POST.get('email_id')

        print(request.POST)

        error_msg = ''

        if len(u_name) == 0 or len(u_name) > 100:
            error_msg = 'Username not valid'

        if len(password) == 0 or len(password) < 10:
            error_msg = 'Password length must be equal or greater than 10'

        if len(error_msg) > 0:
            return render(request, 'appjournal/signup.html', {'error_msg': error_msg})
        else:
            user = User(user_name=u_name, mail_id=mail_id,
                        password=make_password(password))
            # redirect to login
            user.save()
            return redirect('/appjournal/login')
    return render(request, 'appjournal/signup.html')


def login(request):
    if request.session.has_key('email'):
        print('My email is :' + request.session['email'])
        return redirect('/appjournal/profile')
    error_msg = ''
    if request.method == 'POST':
        u_name = request.POST.get('name')
        password = request.POST.get('password')
        mail_id = request.POST.get('email_id')

        error_msg = ''

        if len(error_msg) > 0:
            return render(request, 'appjournal/login.html', {'error_msg': error_msg})
        else:
            try:
                u = User.objects.get(mail_id=mail_id)
                user_give_password = password
                db_stored_password = u.password
                if check_password(user_give_password, db_stored_password):
                    request.session['email'] = mail_id
                    return redirect('/appjournal/profile')
                else:
                    return render(request, 'appjournal/login.html', {'error_msg': 'Password is wrong'})

            except User.DoesNotExist:
                return render(request, 'appjournal/login.html', {'error_msg': 'User does not exist'})

            return redirect('/appjournal/login')

    return render(request, 'appjournal/login.html')


def profile(request):

    if not request.session.has_key('email'):
        return redirect('/appjournal/login')

    user_email = request.session['email']

    try:
        user = User.objects.get(mail_id=user_email)
        context = {
            'user': user
        }
        return render(request, 'appjournal/profile.html', context)
    except User.DoesNotExist:
        print('User does not exist')
        return redirect('/appjournal/login')

    # uname=request.get(mail_id)
    # u=User.object.get request.session['email'] = u.mail_id
    # if i am not logged in, redirect to login
    # if i am logged in, fetch the user from user database
    # pass the data to the below render request
# , {
      #  'user': ''


def logout(request):
    # Changes
    # from session you delete the user
    del request.session['email']
    return redirect('/appjournal/login')

def journal_create(request):
    if  not request.session.has_key('email'):
        return redirect('/appjournal/login')
    else:
        summary = request.POST.get('summary')
        email = request.session['email']
        user = User.objects.get(mail_id=email)

        new_journal = Journal(user=user, summary=summary)
        
        new_journal.save()
        
        

    return redirect('/appjournal/profile')

def journal_list(request):
    email=request.session['email']
    user=User.objects.get(mail_id=email)
    journals = user.journal_set.all()
    
    context = {
        'journals': journals,
        
    }

    return render(request, 'appjournal/list.html', context)
