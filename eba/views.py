from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from forms import LoginForm

def index_page(request): 
    app_name = 'EBA'
    
    if request.method == 'POST':
        login_form = LoginForm(request.POST) 
    else:
        login_form = LoginForm()
    
    if login_form and login_form.is_valid():
        username = login_form['username']
        password = login_form['password']

    variables = RequestContext(request, {
        'login_form': login_form,
        'app_name': app_name 
    })
    return render_to_response('index.html', variables)
