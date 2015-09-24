from forms import LoginForm

from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.utils.translation import ugettext as _ 
from forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.forms import User
from models import Event
import json

def index_page(request): 
    """
    Loads the login page and contains the validations to 
    authenticate an user.
    """

    if request.method == 'POST':
        login_form = LoginForm(request.POST) 
        user = None 
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
        
        if user is not None:
            # the password verified for the user
            if user.is_active:
                return HttpResponse(_("User is valid, active and authenticated"))
            else:
                return HttpResponse(_("The password is valid, but the account has been disabled!"))
        else:
            # the authentication system was unable to verify the username and password
            return HttpResponse(_("The username and password are incorrect."))
    else:
        login_form = LoginForm()

    variables = RequestContext(request, {
        'login_form': login_form,
        'login_title': _("Login") 
    })
    return render_to_response('index.html', variables)
"""
Esta vista realiza la consulta de todos los eventos en la base de datos filtrados por el nombre del evento
y los trae como un JSON

"""
def all_events(request):
    list_events = Event.objects.all()
    list_response = []

    for event in list_events:            
        list_response.append(event.name)

    json_response = json.dumps({
        "list_event_names": list_response
    })
    return HttpResponse(json_response)
"""
Esta vista realiza la consulta de todos los usuarios en la base de datos filtrado por el nickname 
y los trae como un JSON

"""
def all_users(request):
    list_users = User.objects.all()
    list_response = []

    for user in list_users:            
        list_response.append(user.username)

    json_response = json.dumps({
        "list_user_names": list_response
    })
    return HttpResponse(json_response)