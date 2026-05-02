from django.shortcuts import render,HttpResponse
from  feedback.models import  Feedback
import datetime
# Create your views here.
def view_feedback(request):
    obj = Feedback.objects.all()
    context = {'ok': obj}
    return render(request, 'feedback/view_feedback.html', context)

from rest_framework.views import APIView,Response
from .serializer import android_serializer
from .models import Review
class feedback(APIView):
    def post(self,request):
        ob=Feedback()
        ob.date=datetime.datetime.today()
        ob.time=datetime.datetime.now()
        ob.comment=request.data['comment']
        ob.rating=request.data['review']
        ob.user_id=request.data['user_id']
        ob.save()
        return HttpResponse('jhg')

class review(APIView):
    def post(self, request):
        ob = Review()
        ob.date = datetime.datetime.today()
        ob.review = request.data['review']
        ob.user_id = request.data['user_id']   # logged user
        ob.worker_id = request.data['worker_id']  # ✅ from dropdown
        ob.save()
        return HttpResponse('success')
from worker.models import Worker
from worker.serializer import android_serializer

class get_workers(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = android_serializer(workers, many=True)
        return Response(serializer.data)

def view_review(request):
    ss=request.session['u_id']
    ob=Review.objects.filter(review_id=ss)
    c={
        'k':ob
    }
    return render(request,'feedback/view review.html',c)