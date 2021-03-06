"""eba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'eba.views.index_page', name='index_page'),
    url(r'^json_all_events/$', 'eba.views.json_all_events', name='all_events'),
    url(r'^json_conferences_by_event/$', 'eba.views.json_conferences_by_event', name='conferences_by_event'),
    url(r'^json_login/$', 'eba.views.json_login', name='login'),
    url(r'^json_register/$', 'eba.views.json_register', name='register'),
    url(r'^json_all_lecturers/$', 'eba.views.json_all_lecturers', name='all_lecturers'),
    url(r'^json_event_registration/$', 'eba.views.json_event_registration', name='event_registration'),
    url(r'^json_is_user_inscribed/$', 'eba.views.json_is_user_inscribed', name='is_user_inscribed'),
    url(r'^json_score_conference/$', 'eba.views.json_score_conference', name='score_conference'),
    url(r'^json_all_conference_comments/$', 'eba.views.json_all_conference_comments', name='all_conference_comments'),
    url(r'^json_my_events/$', 'eba.views.json_my_events', name='all_my_events'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

