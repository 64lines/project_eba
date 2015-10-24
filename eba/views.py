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
from models import Conference
from models import Attendant
from django.core import serializers
import json

def index_page(request):
    return render_to_response('index.html')

# JSON service to get events list
def json_all_events(request):
    events_list = Event.objects.all()
    json_response = serializers.serialize('json', events_list)
    return HttpResponse(json_response)
    
# JSON service to get conferences by event
def json_conferences_by_event(request):
    conferences_list = []
    id_event = request.REQUEST.get("event", None)
     
    if id_event:
        conferences_list = Conference.objects.filter(event__id=id_event)

    json_response = serializers.serialize('json', conferences_list)
    return HttpResponse(json_response)

# Login an user using its email and password.
def json_login(request):
    logged_user = None
    email = request.REQUEST.get("email", None)
    password = request.REQUEST.get("password", None)
    
    search_user = User.objects.filter(email=email)
    if search_user:
        username = search_user.first().username
        logged_user = authenticate(username=username, password=password) 

    if logged_user:
        json_response = serializers.serialize('json', [logged_user])
    else:
        json_response = "Error: Login failed"

    return HttpResponse(json_response)

def json_event_registration(request):
    status = ""
    selected_user = None
    user_id = request.REQUEST.get("user", None)
    code = request.REQUEST.get("code", None)

    events_qs = Event.objects.filter(code=code)
    event = events_qs.first() if events_qs else None
    
    user_qs = User.objects.filter(pk=user_id)
    if user_qs:
        selected_user = user_qs.first()

    if event: 
        conferences_list = Conference.objects.filter(event=event)
        for conference in conferences_list:
            attendant_qs = Attendant.objects.filter(user=selected_user) 

            if not attendant_qs:
                Attendant.objects.create(user=selected_user, conference=conference)
                status = "Successful Event Registration"
    else:
        status = "Error: Event registration failed"

    return HttpResponse(status)
        
# Register a new user
def json_register(request):
    status = ""
    email = request.REQUEST.get("email", None)
    password = request.REQUEST.get("password", None)
    first_name = request.REQUEST.get("first_name", None)
    last_name = request.REQUEST.get("last_name", None)

    if email and password and first_name and last_name:
        username = email.split("@")[0]
        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        status = "Successful registration"
    else:
        status = "Error: Failed registration" 

    return HttpResponse(status)

def json_all_users(request):
    list_users = User.objects.all()
    list_response = []

    for user in list_users:            
        list_response.append(user.username)

    json_response = json.dumps({
        "list_user_names": list_response
    })
    return HttpResponse(json_response)
