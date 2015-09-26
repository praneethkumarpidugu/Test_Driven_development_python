"""
superlists URL Configuration

The `urlpatterns` lists routes URLs to views.
Examples:
Function views
	1.Add an import: from my_app import views
	2.Add a URL to urlpatterns: url(r'^$', views.home, name='home')
Class Based views
	1. Add an import: from my_app.views import Home
	2. Add a URL to urlpatterns: url(r'^$', Home.as_view(), name='home')
Include another URLconf
	1.Add an import: from blog import urls as blog_urls
	2.Add a URL to urlpatterns: url(r'^blog/', include(blog_urls))

"""
from lists import views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'examplelists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home_page, name='home'),
    #url(r'^admin/', include(admin.site.urls)),
]
