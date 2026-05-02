from django.shortcuts import render,HttpResponseRedirect
# Create your views here.


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj=Login.objects.filter(username=username,password=password)
        # print(len(obj))
        tp=""
        for ob in obj:
            tp=ob.type
            u_id=ob.u_id
            if tp == "admin":
                request.session["u_id"]=u_id
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "worker":
                request.session["u_id"] = u_id
                return HttpResponseRedirect('/temp/worker/')
            else:
                msg = "Username or password is wrong.please try again."
                context={
                    'm': msg
                }
                return render(request,'login/login.html',context)
    return render(request,"login/login.html")

from rest_framework.views import APIView, Response
from login.serializer import android_serializers
from login.models import Login
# from student.models import Student
from django.http import HttpResponse

class login_app(APIView):
    def get(self, request):
        obj = Login.objects.all()
        ser = android_serializers(obj, many=True)
        return Response(ser.data)

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        obj = Login.objects.filter(username=username, password=password)
        ser = android_serializers(obj, many=True)
        return Response(ser.data)