# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import AppointmentModel,RatingModel
from corporation.models import AppointmentHourModel,CorpLocModel,ReservedHourModel
from individual.models import IndividualModel
from datetime import date,datetime,timedelta
from .forms import AppointmentForm,iRatingForm,cRatingForm
from django import forms



def appointment_list(request,appointment_id):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!='':
            appointments = AppointmentModel.objects.filter(res_hour_id__corp_loc_id__corporation=request.user.corporation_id)
        elif request.user.individual_id!='':
            appointments=AppointmentModel.objects.filter(person_id=request.user.individual_id)
        return render(request,'list_any.html',{'title':'Appointment List','list1':appointments,'item_link':'http://localhost/record/make_appointment/','item_title':'Make Appointment'})
    else:
        return redirect('http://localhost/')

def make_appointment(request):
    if request.user.__str__()!='AnonymousUser':
        if request.user.individual_id_id!='':
            form1=AppointmentForm()
            if request.POST:
                form1=AppointmentForm(request.POST)
                if form1.is_valid():
                    form1.add(request)
            return render(request,'form.html',{'form':form1})
        return redirect('http://localhost/')
    else:
        return redirect('http://localhost/')

def find_available_appointments(request):
    if request.user.__str__()!='AnonymousUser':
        if request.user.individual_id!='':
            list1=AppointmentHourModel.objects.filter(date__range=(datetime.today()+timedelta(hours=24),datetime.today()+timedelta(hours=720)))
            return render(request,'list_any.html',{'title':'Appointment Hours','list1':list1})
    else:
        return redirect('http://localhost/')

def busy_day(request):
    if request.user.__str__()!='AnonymousUser':
        app_list=AppointmentModel.objects.filter(res_hour_id__date__range=(datetime.today() - timedelta(hours=360),
                                                                           datetime.today() + timedelta(hours=360)))
        day_dict={}
        for app in app_list:
            if app.res_hour_id.date not in day_dict:
                day_dict[app.res_hour_id.date]=1
            else:
                day_dict[app.res_hour_id.date] += 1
        day_list=[]
        for item in day_dict:
            day_list.append(str(item)+' - '+str(day_dict[item]))
        return render(request, 'list_any.html', {'title': 'Most Busy Day', 'list1': sorted(day_list),
                                                 'item_link': 'http://localhost/corporation/appointment_list/',
                                                 'item_title': 'Appointment List'})
    else:
        return redirect('http://localhost/')

def show_close_corp(request,degree):
    if request.user.__str__()!='AnonymousUser':
        if request.user.individual_id!='':
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
            return render(request, 'list_any.html', {'title': x, 'list1': list1})
    else:
        return redirect('http://localhost/')

def show_appointments(request,date):
    if request.user.__str__()!='AnonymousUser':
        if date[0]=='c':
            app_list = AppointmentModel.objects.filter(res_hour_id__corp_loc_id__corporation=request.user.corporation_id, )
        elif date[0]=='i':
            app_list = AppointmentModel.objects.filter(person_id=request.user.individual_id)
        else:
            app_list = AppointmentModel.objects.all()
        i_c=date[0]
        date=date[1:]
        if len(date)==4:
            app_list=app_list.filter(res_hour_id__date__year=date)
            x='Appointment List Date: '+date
            y='http://localhost/individual/appointment_list/'+i_c
            z='Appointment List'
        elif len(date)==2:
            app_list = app_list.filter(res_hour_id__date__month=date)
            x='Appointment List Date: '+date
            y='http://localhost/individual/appointment_list/'+i_c
            z='Appointment List'
        elif len(date)==7:
            month,year=date.split('-')
            app_list = app_list.filter(res_hour_id__date__year=year,res_hour_id__date__month=month)
            x='Appointment List Date: '+date
            y='http://localhost/individual/appointment_list/'+i_c
            z='Appointment List'
        elif len(date)==3 and date[-1]=='w':
            date=str(datetime.today().year)+' '+date[:2]+' w1'
            res = datetime.strptime(date, "%Y %W w%w")
            app_list = app_list.filter(res_hour_id__date__range=(res,res+timedelta(days=7)))
            x='Appointment List Date: '+date[0:]
            y='http://localhost/individual/appointment_list/'+i_c
            z='Appointment List'
        elif len(date)==1:
            if date=='o':
                app_list=app_list.filter(res_hour_id__date__range=(datetime.today()-timedelta(hours=720),datetime.today()))
                x='Appointment List Old'
                y='http://localhost/individual/appointment_list/'+i_c+'n'
                z='Appointment List Next'
            elif date=='n':
                app_list = app_list.filter(
                    res_hour_id__date__range=(datetime.today() + timedelta(hours=24), datetime.today() + timedelta(hours=720)))
                x='Appointment List Next'
                y='http://localhost/individual/appointment_list/'+i_c+'o'
                z='Appointment List Old'
            else:
                x='Appointment List'
                y='http://localhost/individual/appointment_list/'+i_c+'n'
                z='Appointment List Next'
        else:
            x='Appointment List'
            y='http://localhost/individual/appointment_list/'+i_c+'n'
            z='Appointment List Next'
        return render(request, 'list_any.html', {'title':x,
                                                 'list1': app_list,
                                                 'item_link':y,
                                                 'item_title':z})
    else:
        return redirect('http://localhost/')

def most_popular_service(request,date):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!='':
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
            return render(request, 'list_any.html', {'title': 'Appointment List', 'list1': service_dict.items(),'item_link': 'http://localhost/corporation/appointment_list_next/','item_title': 'Appointment List Next'})
    else:
        return redirect('http://localhost/')

def rating_list(request,rating_id):
    if request.user.__str__()!='AnonymousUser':
        if rating_id:
            ratings=[RatingModel.objects.get(pk=rating_id)]
        else:
            if request.user.corporation_id!='':
                ratings=RatingModel.objects.filter(corp_id=request.user.corporation_id)
                x='Corporation Rating List'
                y='http://localhost/record/rate/i'
                z='Rate a Customer'
            elif request.user.individual_id != '':
                ratings = RatingModel.objects.filter(ind_id=request.user.individual_id)
                x='Individual Rating List'
                y='http://localhost/record/rate/c'
                z='Rate a Corporation'
        return render(request, 'list_any.html', {'title': x,
                                                 'list1': ratings,
                                                 'item_link': y,
                                                 'item_title': z})
    else:
        return redirect('http://localhost/')

def rate(request,i_c):
    if request.user.__str__()!='AnonymousUser':
        if i_c=='i':
            form1=iRatingForm()
            if request.POST:
                form1=iRatingForm(request.POST)
                if form1.is_valid():
                    form1.add(request)
            return render(request,'form.html',{'title':'Rate ',
                                               'form':form1})
        elif i_c=='c':
            form1=cRatingForm()
            form1['corp_id'].widget=forms.HiddenInput
            if request.POST:
                form1=cRatingForm(request.POST)
                if form1.is_valid():
                    form1.add(request)
            return render(request,'form.html',{'title':'Rate ',
                                               'form':form1})
        else:
            return redirect('http://localhost/record/rating_list/')
    else:
        return redirect('http://localhost/')


def most_appointer(request,id):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!='':
            all_apps=AppointmentModel.objects.filter(res_hour_id__corp_loc_id__corporation=request.user.corporation_id)
            ind_dict={}
            for x in all_apps:
                if x.person_id not in ind_dict:
                    ind_dict[x.person_id]=1
                else:
                    ind_dict[x.person_id]+=1
            return render(request, 'list_any.html', {'title': 'Most Appointmenter List', 'list1': ind_dict.items(),
                                             'item_link': 'http://localhost/corporation/appointment_list/',
                                             'item_title': 'Appointment List'})
    else:
        return redirect('http://localhost/')


def busy_hour(request,time):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!='':
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
                rh_list.append((str(h)+':'+str(m),rh_dict[a]))
            return render(request, 'list_any.html', {'title': 'Most Busy Hours', 'list1': rh_list,
                                             'item_link': 'http://localhost/corporation/appointment_list/',
                                             'item_title': 'Appointment List'})
    else:
        return redirect('http://localhost/')


def complain(request,id):
    pass