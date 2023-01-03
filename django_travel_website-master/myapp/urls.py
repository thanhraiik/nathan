"""samsung URL Configurationmyapp/urls.py

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""






from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView,ListView
from .import views
from myapp.models import package



urlpatterns = [
path('packages/',ListView.as_view(model=package,template_name="package.html")),


    #
    #
    # url(r'^register$', views.signin, name='Register'),
    # url(r'^registerwithus$', views.register, name='registerr'),
    # #
    # url(r'^indexo$', views.contact,name='conact'),
    # url(r'^contact', views.indexo,name='contact'),
    path('contact/', views.contact1, name='contact1'),
    path('login/', views.signin, name='signin'),
    path('logged/', views.loginforms,name='loginprocess'),
    path('logout/', views.logout, name='logout'),

    path('index/', TemplateView.as_view(template_name='index.html')),
    path('contact/', TemplateView.as_view(template_name='contact.html')),
    path('register/', TemplateView.as_view(template_name='register.html')),
    path('VARANASI/', TemplateView.as_view(template_name='varanasi.html')),
    path('MANALI/', TemplateView.as_view(template_name='manali.html')),
    path('KASHMIR/', TemplateView.as_view(template_name='kashmir.html')),
    path('RAJASTHAN/', TemplateView.as_view(template_name='rajasthan.html')),
    path('gallery/', TemplateView.as_view(template_name='gallery.html')),
    path('login/', TemplateView.as_view(template_name='login.html')),

    path('loggedin/', TemplateView.as_view(template_name='loggedin.html')),
    path('contact_lo/', TemplateView.as_view(template_name='contact_lo.html')),
    path('payment/', TemplateView.as_view(template_name='payment.html')),
    path('hotdeals/', TemplateView.as_view(template_name='hotdeals.html')),
    path('packages/', TemplateView.as_view(template_name='package.html')),
    path('rajasthan_lo/', TemplateView.as_view(template_name='rajasthan_lo.html')),
    path('varanasi_lo/', TemplateView.as_view(template_name='varanasi_lo.html')),
    path('manali_lo/', TemplateView.as_view(template_name='manali_lo.html')),
    path('kashmir_lo/', TemplateView.as_view(template_name='kashmir_lo.html')),
    path('SOUTH INDIA/', TemplateView.as_view(template_name='south.html')),
    path('NORTH/', TemplateView.as_view(template_name='north.html')),
    path('NORTH EAST/', TemplateView.as_view(template_name='northeast.html')),
    path('GOA/', TemplateView.as_view(template_name='goa.html')),
    path('logout/', TemplateView.as_view(template_name='logout.html')),



    path('base/', TemplateView.as_view(template_name='base.html')),

    #
    # url(r'^login/', TemplateView.as_view(template_name='login.html')),
    # url(r'^ne',views.loginf,name='newlog'),

    # url(r'^$', views.sign, name='sign'),
    #
    # url(r'^contact$', views.contact, name='contact'),
    # url(r'^contact$', views.contact, name='contact')

]
