# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import AppointmentModel,RatingModel
from corporation.models import AppointmentHourModel,CorpLocModel,ReservedHourModel
from datetime import date,datetime,timedelta
from .forms import AppointmentForm,iRatingForm,cRatingForm
from django import forms
import json



def appointment_list(request,appointment_id):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!=None:
            appointments = AppointmentModel.objects.filter(res_hour_id__corp_loc_id__corporation=request.user.corporation_id)
        elif request.user.individual_id!=None:
            appointments=AppointmentModel.objects.filter(person_id=request.user.individual_id)
        return render(request,'records/appointment_list.html',{'title':'List of All Appointment','list1':appointments,'item_link':'http://127.0.0.2:8000/record/make_appointment/','item_title':'Make Appointment'})
    else:
        return redirect('http://127.0.0.2:8000/')

def make_appointment(request):
    if request.user.__str__()!='AnonymousUser':
        if request.user.individual_id!=None:
            form1=AppointmentForm()
            if request.POST:
                form1=AppointmentForm(request.POST)
                if form1.is_valid():
                    form1.add(request)
            return render(request,'records/make_appointment.html',{'form':form1,'title':'Make An Appointment'})
        return redirect('http://127.0.0.2:8000/')
    else:
        return redirect('http://127.0.0.2:8000/')

def find_available_appointments(request):
    if request.user.__str__()!='AnonymousUser':
        if request.user.individual_id!=None:
            list1=AppointmentHourModel.objects.filter(date__range=(datetime.today()+timedelta(hours=24),datetime.today()+timedelta(hours=720)))
            return render(request,'records/find_available_appointments.html',{'title':'Appointment Hours','list1':list1})
        else:
            return redirect('http://127.0.0.2:8000/')
    else:
        return redirect('http://127.0.0.2:8000/')

def busy_day(request):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!=None:
            app_list = AppointmentModel.objects.filter(res_hour_id__date__range=(datetime.today() - timedelta(hours=3600),
                                                                                 datetime.today() + timedelta(hours=3600)))
            day_dict = {}
            for app in app_list:
                if app.res_hour_id.date not in day_dict:
                    day_dict[app.res_hour_id.date] = 1
                else:
                    day_dict[app.res_hour_id.date] += 1
            data = []
            for item in day_dict:
                data.append({"label":str(item),"value":str(day_dict[item])})
            day_list=[]
            for item in day_dict:
                day_list.append(str(item)+' - '+str(day_dict[item]))

            data=json.dumps(data)
            return render(request, 'records/busy_day.html', {'data1':data,
                                                  'title':'Most Busy Days',
                                                  'yname':'Number of Appointment',
                                                   'subtitle':'Frequency of Busy Days',
                                                  'ynamesuffix':' Times',
                                                   'list1': sorted(day_list),
                                                 'item_link': 'http://127.0.0.2:8000/corporation/appointment_list/',
                                                 'item_title': 'Appointment List'})
        else:
            return redirect('http://127.0.0.2:8000/')
    else:
        return redirect('http://127.0.0.2:8000/')

def show_close_corp(request,degree):
    if request.user.__str__()!='AnonymousUser':
        if request.user.individual_id!=None:
            loc=request.user.individual_id.ind_loc_id
            corp_loc=CorpLocModel.objects.all()
            list1=[]
            if degree=='p':
                for corp in corp_loc:
                    if corp.location.district_id.town_id.province_id==loc.district_id.town_id.province_id:
                        list1.append(corp)
                x='Corporations is in Same City'
            elif degree=='t':
                for corp in corp_loc:
                    if corp.location.district_id.town_id==loc.district_id.town_id:
                        list1.append(corp)
                x='Corporations is in Same Town'
            elif degree=='d':
                for corp in corp_loc:
                    if corp.location.district_id==loc.district_id:
                        list1.append(corp)
                x='Corporations is in Same District'
            elif degree=='s':
                for corp in corp_loc:
                    if corp.location==loc:
                        list1.append(corp)
                x='Corporations is in Same Street'
            else:
                x='There is no corporation close to you'
            return render(request, 'records/show_close_corp.html', {'title': x, 'list1': list1})
        else:
            return redirect('http://127.0.0.2:8000/')
    else:
        return redirect('http://127.0.0.2:8000/')

def show_appointments(request,date):
    if request.user.__str__()!='AnonymousUser':
        if date[0]=='c':
            if request.user.corporation_id!=None:
                app_list = AppointmentModel.objects.filter(res_hour_id__corp_loc_id__corporation=request.user.corporation_id, )
            else:
                return redirect('http://127.0.0.2:8000/')
        elif date[0]=='i':
            if request.user.individual_id!=None:
                app_list = AppointmentModel.objects.filter(person_id=request.user.individual_id)
            else:
                return redirect('http://127.0.0.2:8000/')
        else:
            return redirect('http://127.0.0.2:8000/')
        i_c=date[0]
        date=date[1:]
        if len(date)==4:
            app_list=app_list.filter(res_hour_id__date__year=date)
            x='Appointment List Date: '+date
            y='http://127.0.0.2:8000/individual/appointment_list/'+i_c
            z='Appointment List'
        elif len(date)==2:
            app_list = app_list.filter(res_hour_id__date__month=date)
            x='Appointment List Date: '+date
            y='http://127.0.0.2:8000/individual/appointment_list/'+i_c
            z='Appointment List'
        elif len(date)==7:
            month,year=date.split('-')
            app_list = app_list.filter(res_hour_id__date__year=year,res_hour_id__date__month=month)
            x='Appointment List Date: '+date
            y='http://127.0.0.2:8000/individual/appointment_list/'+i_c
            z='Appointment List'
        elif len(date)==3 and date[-1]=='w':
            date=str(datetime.today().year)+' '+date[:2]+' w1'
            res = datetime.strptime(date, "%Y %W w%w")
            app_list = app_list.filter(res_hour_id__date__range=(res,res+timedelta(days=7)))
            x='Appointment List Date: '+date[0:]
            y='http://127.0.0.2:8000/individual/appointment_list/'+i_c
            z='Appointment List'
        elif len(date)==1:
            if date=='o':
                app_list=app_list.filter(res_hour_id__date__range=(datetime.today()-timedelta(hours=720),datetime.today()))
                x='Appointment List Old'
                y='http://127.0.0.2:8000/individual/appointment_list/'+i_c+'n'
                z='Appointment List Next'
            elif date=='n':
                app_list = app_list.filter(
                    res_hour_id__date__range=(datetime.today() + timedelta(hours=24), datetime.today() + timedelta(hours=720)))
                x='Appointment List Next'
                y='http://127.0.0.2:8000/individual/appointment_list/'+i_c+'o'
                z='Appointment List Old'
            else:
                x='Appointment List'
                y='http://127.0.0.2:8000/individual/appointment_list/'+i_c+'n'
                z='Appointment List Next'
        else:
            x='Appointment List'
            y='http://127.0.0.2:8000/individual/appointment_list/'+i_c+'n'
            z='Appointment List Next'
        return render(request, 'records/show_appointments.html', {'title':x,
                                                 'list1': app_list,
                                                 'item_link':y,
                                                 'item_title':z})
    else:
        return redirect('http://127.0.0.2:8000/')

def most_popular_service(request,date):
    if request.user.__str__()!='AnonymousUser':
        app_list=AppointmentModel.objects.filter(res_hour_id__corp_loc_id__corporation=request.user.corporation_id)
        if len(date)==4:
            app_list=app_list.filter(res_hour_id__date__year=date)
        elif len(date)==2:
            app_list = app_list.filter(res_hour_id__date__month=date)
        elif len(date)==7:
            month,year=date.split('-')
            app_list = app_list.filter(res_hour_id__date__year=year,res_hour_id__date__month=month)
        elif len(date)==3 and date[-1]=='w':
            date=str(datetime.today().year)+' '+date[:2]+' w1'
            res = datetime.strptime(date, "%Y %W w%w")
            app_list = app_list.filter(res_hour_id__date__range=(res,res+timedelta(days=7)) )
        service_dict={}
        for item in app_list:
            if item.service not in service_dict:
                service_dict[item.service]=1
            else:
                service_dict[item.service]+=1
        data=[]
        for y,z in service_dict.items():
            data.append({"label":str(y),"value":str(z)})
        data=json.dumps(data)
        return render(request, 'records/most_appointer.html', {'data1':data,
                                              'title':'Most Popular Services',
                                              'yname':'Number of Usage',
                                               'subtitle':'',
                                              'ynamesuffix':' Times',
                                               'list1': service_dict.items(),
                                             'item_link': 'http://127.0.0.2:8000/main/service_list/',
                                             'item_title': 'Service List'})

    else:
        return redirect('http://127.0.0.2:8000/')

def rating_list(request,rating_id):
    if request.user.__str__()!='AnonymousUser':
        if rating_id:
            ratings=[RatingModel.objects.get(pk=rating_id)]
        else:
            if request.user.corporation_id!=None:
                ratings=RatingModel.objects.filter(corp_id=request.user.corporation_id)
                x='Corporation Rating List'
                y='http://127.0.0.2:8000/record/rate/i'
                z='Rate a Customer'
            elif request.user.individual_id != '':
                ratings = RatingModel.objects.filter(ind_id=request.user.individual_id)
                x='Individual Rating List'
                y='http://127.0.0.2:8000/record/rate/c'
                z='Rate a Corporation'
        return render(request, 'records/rating_list.html', {'title': x,
                                                 'list1': ratings,
                                                 'item_link': y,
                                                 'item_title': z})
    else:
        return redirect('http://127.0.0.2:8000/')

def rate(request,i_c):
    if request.user.__str__()!='AnonymousUser':
        if i_c=='i':
            form1=iRatingForm()
            if request.POST:
                form1=iRatingForm(request.POST)
                if form1.is_valid():
                    form1.add(request)
            return render(request,'records/rate.html',{'title':'Rate ',
                                               'form':form1})
        elif i_c=='c':
            form1=cRatingForm()
            form1['corp_id'].widget=forms.HiddenInput
            if request.POST:
                form1=cRatingForm(request.POST)
                if form1.is_valid():
                    form1.add(request)
            return render(request,'records/rate.html',{'title':'Rate ',
                                               'form':form1})
        else:
            return redirect('http://127.0.0.2:8000/record/rating_list/')
    else:
        return redirect('http://127.0.0.2:8000/')

def most_appointer(request,id):
    if request.user.__str__()!='AnonymousUser':
        all_apps=AppointmentModel.objects.all()
        ind_dict={}
        data=[]
        for x in all_apps:
            if x.person_id not in ind_dict:
                ind_dict[x.person_id]=1
            else:
                ind_dict[x.person_id]+=1
        for y,z in ind_dict.items():
            data.append({"label":str(y),"value":str(z)})
        data=json.dumps(data)
        return render(request, 'records/most_appointer.html', {'data1':data,
                                              'title':'Most Appointer List',
                                              'yname':'Number of Appointment',
                                               'subtitle':'',
                                              'ynamesuffix':' Times',
                                               'list1': ind_dict.items(),
                                             'item_link': 'http://127.0.0.2:8000/corporation/appointment_list/',
                                             'item_title': 'Appointment List'})

    else:
        return redirect('http://127.0.0.2:8000/')

def busy_hour(request,time):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!=None:
            all_rhs=ReservedHourModel.objects.filter(corp_loc_id__corporation=request.user.corporation_id)
            rh_dict={}
            for i in range(0,1440):
                rh_dict[i]=0
            for x in all_rhs:
                y=x.start_time.hour*60+x.start_time.minute
                z=x.end_time.hour*60+x.end_time.minute
                for k in range(y,z):
                    rh_dict[k]+=1
            rh_list=[]
            for a in rh_dict:
                h=a/60
                m=a%60
                rh_list.append((str(h).split('.')[0]+':'+str(m),rh_dict[a]))
            data=[]
            for y,z in rh_list:
                data.append({"label":str(y),"value":str(z)})
            data=json.dumps(data)
            return render(request, 'records/busy_hour.html', {'data1':data,
                                                      'title':'Most Busy Hours',
                                                  'yname':'Number of Appointment',
                                                   'subtitle':'',
                                                  'ynamesuffix':' Times',
                                                   'list1': rh_list,
                                                 'item_link': 'http://127.0.0.2:8000/corporation/appointment_list/c',
                                                 'item_title': 'Appointment List'})
        else:
            return redirect('http://127.0.0.2:8000/')
    else:
        return redirect('http://127.0.0.2:8000/')

def complain(request,id):
    pass

