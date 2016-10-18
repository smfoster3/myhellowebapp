from django.conf.urls import include, url
from django.contrib import admin
from collection import views
from django.views.generic import TemplateView



urlpatterns = [
	url(r'^$', views.index, name='home'),
	
	url(r'^about/$',
	
	TemplateView.as_view(template_name='about.html'),
		name='about'),
		
		url(r'^contact/$',
	
	TemplateView.as_view(template_name='contact.html'),
		name='contact'),
		
	
	
    url(r'^admin/', admin.site.urls),
    
    
    
]
