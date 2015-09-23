from forms import LoginForm

from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.utils.translation import ugettext as _ 


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
