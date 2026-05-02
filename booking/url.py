from django.urls import path,re_path
from booking import views

urlpatterns=[
    path('view/',views.MyBookings.as_view()),
    path('book/',views.BookWorker.as_view()),
    path('vie_web/',views.booking_web),
    path('status/',views.status.as_view()),
    path('accept/<int:idd>',views.accept),
    path('reject/<int:idd>',views.reject),





]