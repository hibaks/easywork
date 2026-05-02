from django.shortcuts import render ,HttpResponse
from user.models import User
# Create your views here.
from rest_framework.views import APIView,Response
from .serializer import android_serializer
# Create your views here.
from login.models import Login



class regg(APIView):
    def post(self,request):
        obj=User()
        obj.name=request.data['name']
        obj.email = request.data['email']
        obj.username = request.data['username']
        obj.phone= request.data['phone']
        obj.address = request.data['address']
        obj.password = request.data['password']
        obj.status='pending'
        obj.save()
        ob=Login()
        ob.username=obj.username
        ob.password=obj.password
        ob.type='user'
        ob.u_id=obj.user_id
        ob.save()
        return HttpResponse('reg')

from .serializer import android_serializer
class ccc(APIView):
    def post(self,request):
        ob=User.objects.filter(user_id=request.data['usid'])
        ser=android_serializer(ob,many=True)
        return Response(ser.data)

class update(APIView):
    def post(self,request):
        ob=User.objects.get(user_id=request.data['usid'])
        ob.status = "pending"
        ob.address = request.data['address']
        ob.username = request.data['username']
        ob.name = request.data['name']
        ob.email = request.data['email']
        ob.password = request.data['password']
        ob.phone = request.data['phone']

        ob.save()
        return HttpResponse("yes")
def vcc(request):
    obj=User.objects.all()
    context={'ok': obj}
    return render(request, 'user/user_view.html', context)