from django.conf.urls import url,include
from mainapp import views

#TEMPLATE TAGGING
app_name='mainapp'

urlpatterns = [
    url(r'^reg/$',views.reg,name='reg'),
    url(r'^user_login/$',views.user_login,name='user_login'),
     ]
