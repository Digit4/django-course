from django.conf.urls import url
from newapp import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^register/', views.register_view, name='register'),
	url(r'^logout/', views.user_logout, name='userlogout'),
	url(r'^special/', views.special, name='special'),
	url(r'^login/', views.user_login, name='userlogin')

]
