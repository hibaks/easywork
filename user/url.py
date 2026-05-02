from django.urls import path,re_path
from user import views

urlpatterns=[

    path('flu/',views.regg.as_view()),
    path('vc/',views.vcc),
    path('view/',views.ccc.as_view()),
    path('update/',views.update.as_view())

]