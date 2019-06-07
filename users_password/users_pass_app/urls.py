from django.conf.urls import url
from users_pass_app import views

# template tagging

app_name = 'users_pass_app'

urlpatterns = [
  url('registeration/' , views.register, name = 'register'),
  url('user_login/', views.user_login, name= 'user_login'),

]
