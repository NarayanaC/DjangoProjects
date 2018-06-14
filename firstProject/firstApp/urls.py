from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static
from firstApp import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


#from django.views.generic import TemplateView



urlpatterns =[

	#path('index/', views.index),  

	url(r'^$',views.home,name='index'),
	url(r'^About/$',views.AboutUs, name='aboutus'),
	url(r'^Register/$',views.RegisterNow, name='register'),
	url(r'^ExtendedView/$',views.ViewExt, name='vext'),
	url(r'^ExtendedDetails/$',views.ExtendInfo, name='ext'),
	url(r'^View_Users/$',views.ViewUsers, name='users'),
	url(r'^Update_User/(?P<id>\d+)/$',views.UpdateUser, name='update'),
	url(r'^Delete_User/(?P<id>\d+)/$',views.DeleteteUser, name='delete'),
	url(r'^signup/$',views.signup, name='signup'),
	# url(r'^login/$', auth_views.login,{'template_name': 'firstApp/login.html'}, name='login'),
	url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^Login/auth/$', views.auth_view, name='hell'),
    # url(r'^upload/csv_upload$',views.csv_files, name='csv'),
    url(r'^upload/csv_files$',views.CSV_files, name='csv'),
     url(r'^upload/add_file$',views.add_csv, name='add_csv'),



	
	#url(r'^$',views.header),

	#url(r'^firstapp/', {'templates:index.html'})
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#urlpatterns  += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#urlpatterns += staticfiles_urlpatterns()





# urlpatterns = patterns('',   
#     (r'^one/$', redirect_to, {'url': '/firstApp/about_us.html/'}),

#     #etc...
# )