from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.utils.translation import ugettext as _ 
from django.contrib.auth import authenticate
from django.contrib.auth.forms import User
from django.core import serializers
from django.http import HttpResponse
from forms import LoginForm
from models import Event
from models import Conference
from models import Attendant
from models import Lecturer
from models import ConferenceScore

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
    id_event = request.GET.get("event", None)
     
    if id_event:
        conferences_list = Conference.objects.filter(event__id=id_event)

    json_response = serializers.serialize(
        'json', 
        conferences_list,
    )
    return HttpResponse(json_response)

# Login an user using its email and password.
def json_login(request):
    logged_user = None
    email = request.GET.get("email", None)
    password = request.GET.get("password", None)
    
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
    user_id = request.GET.get("user", None)
    code = request.GET.get("code", None)
    event_id = request.GET.get("event", None)
    
    if code:
        events_qs = Event.objects.filter(code=code)
    elif event_id:
        events_qs = Event.objects.filter(pk=event_id)
        
    event = events_qs.first() if events_qs else None
    
    user_qs = User.objects.filter(pk=user_id)
    if user_qs:
        selected_user = user_qs.first()

    if event: 
        conferences_list = Conference.objects.filter(event=event)
        attendant_qs = Attendant.objects.filter(
            user=selected_user,
            conference__event=event
        ) 
        for conference in conferences_list:
            if not attendant_qs:
                Attendant.objects.create(user=selected_user, conference=conference)

        status = "Successful Event Registration"
    else:
        status = "Error: Event registration failed"

    return HttpResponse(status)
       
def json_is_user_inscribed(request):
    status = 0
    event = request.GET.get("event", None) 
    user = request.GET.get("user", None)
    
    attendant_qs = Attendant.objects.filter(user=user, conference__event=event)
    
    if attendant_qs:
        status = 1

    return HttpResponse(status)

# Register a new user
def json_register(request):
    status = ""
    email = request.GET.get("email", None)
    password = request.GET.get("password", None)
    first_name = request.GET.get("first_name", None)
    last_name = request.GET.get("last_name", None)

    if email and password and first_name and last_name:
        try:
            username = email.split("@")[0]
            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            status = "Successful registration"
        except:
            status = "Error: Failed registration" 
    else:
        status = "Error: Failed registration" 

    return HttpResponse(status)

def json_all_lecturers(request):
    lecturers_list = Lecturer.objects.all()

    json_response = serializers.serialize(
        'json', 
        lecturers_list,
    )
    return HttpResponse(json_response)

def json_score_conference(request):
    status = "0"
    user_id = request.GET.get("user", None)
    conference_id = request.GET.get("conference", None)
    comment = request.GET.get("comment", None)
    score = request.GET.get("score", None)

    user_qs = User.objects.filter(pk=user_id)
    conference_qs = Conference.objects.filter(pk=conference_id)

    if user_qs:
        user = user_qs.first()

    if conference_qs:
        conference = conference_qs.first()

    if user and conference:
        ConferenceScore.objects.create(
            user=user, 
            conference=conference, 
            comment=comment,
            score=score
        )
        status = "1"

    return HttpResponse(status)

def json_user_events(request):
    user_id = request.GET.get("user", None)
    attendants_list = Attendant.objects.filter(user=user_id)

    events_list = Event.objects.all()
    json_response = serializers.serialize('json', events_list)
    return HttpResponse(json_response)

def json_all_conference_comments(request):
    conference_id = request.GET.get("conference", None)
    conference_list = ConferenceScore.objects.filter(conference__pk=conference_id)
    
    json_response = serializers.serialize(
        'json', 
        conference_list,
    )
    return HttpResponse(json_response)
