from django.shortcuts import render,redirect
from complaint.models import Complaint
import datetime
# Create your views here.
# def post_complaint(request):
#     ss=request.session['u_id']
#     if request.method=='POST':
#         obj=Complaint()
#         obj.customer_id=ss
#         obj.date=datetime.datetime.today()
#         obj.time=datetime.datetime.now()
#         obj.complaint=request.POST.get('Complaint')
#         obj.reply='pending'
#         obj.save()
#     return  render(request,'complaint/post_complaint.html')

import datetime
from django.shortcuts import render
from .models import Complaint
#flutter
# from rest_framework.views import APIView,Response
from django.http import HttpResponseRedirect,HttpResponse
# from.serializers import android_serializers

def post_complaint(request):
    ss=request.session['u_id']
    if request.method == 'POST':
        obj = Complaint()
        obj.worker_id = ss
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.complaint = request.POST.get('Complaint')
        obj.reply = 'pending'
        obj.save()
    return render(request,'complaint/post_complaint.html')



def view_complaint_admin(request):
    obj=Complaint.objects.all()
    context={'ok':obj}
    return  render(request,'complaint/complaint_view_admin.html',context)

def post_reply_admin(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('reply')
        obj.save()
    return render(request,'complaint/reply1.html')

def viewreply_worker(request):
    ss=request.session['u_id']
    obj=Complaint.objects.filter(worker_id=ss)
    context={
        'k':obj
    }
    return render(request,'complaint/view_reply.html',context)

from rest_framework.views import APIView,Response
from .serializer import android_serializer
class view_reply(APIView):
    def post(self, request):
        ob = Complaint.objects.filter(user_id=request.data['user_id'])
        ser = android_serializer(ob, many=True)
        return Response(ser.data)
class complaint(APIView):
    def post(self,request):
        ob=Complaint()
        ob.complaint=request.data['complaint']
        ob.user_id=request.data['user_id']
        ob.date=datetime.datetime.today()
        ob.reply='pending'
        ob.worker_id=1
        ob.save()
        return HttpResponse('abd')