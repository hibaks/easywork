from django.shortcuts import render,HttpResponseRedirect
from worker.models import Worker
from login.models import  Login
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Profile
# Create your views here.
from rest_framework.views import APIView,Response
from .serializer import android_serializer
from temp.serializers import ServiceSerializer
from temp.models import Service
class view(APIView):
    def get(self,request):
        ob=Service.objects.all()
        ser=ServiceSerializer(ob,many=True)
        return Response(ser.data)


def worker(request):
    if request.method == 'POST':
        obj = Worker()
        obj.name = request.POST.get('name')
        obj.skill = request.POST.get('skill')
        obj.specialization = request.POST.get('specialization')
        obj.contact = request.POST.get('contact')
        obj.availability = request.POST.get('availability')
        obj.username = request.POST.get('username')
        obj.password = request.POST.get('password')
        obj.save()

        ob = Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.u_id = obj.worker_id
        ob.type = 'worker'
        ob.save()
        return  HttpResponseRedirect('/login/login/')
    return render(request, 'worker/worker.html')


def vt(request):
    obj=Worker.objects.all()
    context={'ok': obj}
    return render(request, 'worker/view_tech.html', context)
def accept(request,idd):
    ob=Worker.objects.get(worker_id=idd)
    ob.status='accept'
    ob.save()
    return vt(request)

def reject(request,idd):
    ob=Worker.objects.get(worker_id=idd)
    ob.status='reject'
    ob.save()
    return vt(request)
def view_profile(request):
    ss = request.session['u_id']
    obj=Worker.objects.filter(worker_id=ss)
    context={'ok': obj}
    return render(request, 'worker/profile.html', context)
def update(request,idd):

    ob = Worker.objects.get(worker_id=idd)
    context = {'ok': ob}
    if request.method == 'POST':
        obj = Worker.objects.get(worker_id=idd)
        obj.name = request.POST.get('name')
        obj.skill = request.POST.get('sk')
        obj.specialization = request.POST.get('sp')
        obj.contact = request.POST.get('co')
        obj.availability = request.POST.get('av')
        obj.username = request.POST.get('uu')
        obj.password = request.POST.get('pp')
        obj.save()
        return redirect('/worker/view_profile/')
    return render(request,'worker/update.html',context)
# def worker_profile(request):
#     ss = request.session.get('u_id')
#
#     if not worker_id:
#         return redirect('/login/')
#
#     worker = Worker.objects.get(worker_id=ss)
#     profile, created = Profile.objects.get_or_create(user=worker)
#
#     if request.method == 'POST':
#
#         # BIO
#         profile.bio = request.POST.get('bio')
#
#         # IMAGE
#         if request.FILES.get('image'):
#             myfile = request.FILES['image']
#             fs = FileSystemStorage()
#             filename = fs.save(myfile.name, myfile)
#             profile.profile_pic = filename
#
#         # PASSWORD (FIXED)
#         new_password = request.POST.get('new_password')
#
#         if new_password:
#             print("PASSWORD RECEIVED:", new_password)  # DEBUG
#             technician.password = new_password
#             technician.save()
#
#         profile.save()
#         return redirect('edit_profile')
#
#     return render(request, 'profile_view/profile.html', {
#         'tech': technician,
#         'profile': profile
#     })