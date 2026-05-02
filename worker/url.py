from django.urls import path
from . import views
urlpatterns=[
    path('view/',views.view.as_view()),
    path('worker/',views.worker),
    path('view_profile/', views.view_profile),
    path('update/<int:idd>', views.update),
    path('vt/',views.vt),
    path('accept/<int:idd>/', views.accept, name='accept_tech'),
    path('reject/<int:idd>/', views.reject, name='reject_tech'),
]