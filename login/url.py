from django.urls import path, re_path
from login import views

urlpatterns = [

    path('login_app/',views.login_app.as_view()),
    path('login/',views.login,name='login')

]