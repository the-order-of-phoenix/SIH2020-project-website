from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'mysite'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    re_path(r'^(?P<pk>\d+)/update/$',views.sendmail,name="sendmail"),

]
