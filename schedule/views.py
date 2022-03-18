from django.dispatch import receiver
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView# normal view can written API data
from .models import *
import datetime
class InterviewSchedule(APIView):
    def post(self,request):
        date=request.data['date']
        time_start=request.data['time_start']
        time_end=request.data['time_end']
        user_detail_id=request.data['user_detail_id']
        start = datetime.datetime.strptime( time_start,"%I:%M %p").time()
        end = datetime.datetime.strptime(time_end, "%I:%M %p").time()
        schedule=UserSchdulemaaping.objects.create(user_detail_id=user_detail_id,date=date,time_start=start,time_end=end)
        schedule.save()
        return HttpResponse("schedule successfully created")
    def get(self,request):
        candidate_id=request.data['candidate_id']
        interviewer_id=request.data['interviewer_id']
        candidatesch=UserSchdulemaaping.objects.filter(user_detail_id=candidate_id).first()       
        interviewsch=UserSchdulemaaping.objects.filter(user_detail_id=interviewer_id).first()
        if candidatesch.time_start<=interviewsch.time_start:
            interval_start=interviewsch.time_start
        else:
            interval_start=candidatesch.time_start
        if candidatesch.time_end<=interviewsch.time_end:
            interval_end=candidatesch.time_end
        else:
            interval_end=interviewsch.time_end
        interval = datetime.timedelta(minutes=60)
        periods = []
        period_start = interval_start
        while period_start < interval_end:
            period_end = min(period_start + interval, interval_end)
            strtime=period_start.strftime("%Y-%m-%d %H:%M") +"to" + period_end.strftime("%Y-%m-%d %H:%M")
            periods.append(strtime)
            period_start = period_end
        return JsonResponse(periods,safe=False)
