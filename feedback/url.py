from django.urls import path, re_path
from feedback import views

urlpatterns = [
    path('view/', views.view_feedback),
    path('view_review/',views.view_review),
    path('feedback/',views.feedback.as_view()),
    path('review/',views.review.as_view()),
path('get_workers/', views.get_workers.as_view())
]