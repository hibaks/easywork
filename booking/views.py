from django.shortcuts import render
from .models import Book
# Create your views here.
from rest_framework.views import APIView,Response
from .serializer import android_serializer
import datetime
class MyBookings(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        ob = Book.objects.filter(user_id=user_id)
        ser = android_serializer(ob, many=True)
        return Response(ser.data)

class BookWorker(APIView):
    def post(self, request):
        ob = Book()
        ob.user_id = request.data['user_id']
        ob.service_id = request.data['service_id']
        ob.date = datetime.date.today()
        ob.time = datetime.datetime.now().time()
        ob.status = "booked"
        ob.save()
        return Response({"message": "Booked Successfully"})

class status(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        ob = Book.objects.filter(user_id=user_id)
        ser = android_serializer(ob, many=True)
        return Response(ser.data)
def booking_web(reqest):
    ss=reqest.session['u_id']
    obj=Book.objects.filter(service__worker_id=ss)
    c={
        'oo':obj
    }
    return render(reqest,'booking/booking_view.html',c)

def accept(request,idd):
    ob=Book.objects.get(book_id=idd)
    ob.status='accept'
    ob.save()
    return booking_web(request)
def reject(request,idd):
    ob=Book.objects.get(book_id=idd)
    ob.status='reject'
    ob.save()
    return booking_web(request)