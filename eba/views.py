from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader

def index_page(request): 
    app_name = 'EBA'
    variables = RequestContext(request, {
        'app_name': app_name 
    })
    return render_to_response('index.html', variables)
