from django.urls import path,re_path
from . import views

urlpatterns = [
     path('post/',views.post_complaint),
     path('ad/',views.view_complaint_admin),
     re_path('reply1/(?P<idd>\w+)',views.post_reply_admin),
     path('v_reply/',views.viewreply_worker),
     path('view_reply/',views.view_reply.as_view()),
     path('complaint/',views.complaint.as_view())
     # path('v_reply/',views.view_reply)
]