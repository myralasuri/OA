from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from employee.models import Employe, Department, Position, Leaves
from employee.authbackend import AuthBackend
from django.contrib.auth import login
from django.db.models import Q
from django.core import serializers
import pprint
import json
# Create your views here.

def home(request):
    if request.method=='POST':
        uname =  request.POST['username']
        pwd  = request.POST['password']
        # print('uanme : - ', uname, pwd)
        user = AuthBackend.authenticate(request=request, username= uname, password= pwd)
        pos = Position.objects.get(emp = user)
        emptype= 'emp'if pos.position == 'employee' else 'manager'
        print('user: ', user)
        # login(request,user)
        print(request.session)
        request.session['usertype'] =emptype
        request.session['useremail'] = user.email
        return HttpResponseRedirect('OA/{b}/{a}/'.format(a=user.id, b= emptype),)
    return render(request, 'home.html');

def emp(request, id):
    emps = Employe.objects.get(id= id)
    leaves = Leaves.objects.filter(emp = emps)
    # print(leaves)
    print( request.session['useremail'])
    return render(request, 'employee_list.html',
     {'emp': emps, 'leaves': leaves, 'email':request.session['useremail'] })

def manager(request, id):
    if request.method == 'POST':
        pkid = request.POST['leaveid']
        sts = request.POST['setstatus']
        print('pkid : ------------', pkid)
        ob = Leaves.objects.get(pk=pkid)
        ob.status= sts
        ob.save()
        # pprint.pprint(serializers.serialize('json',[ob]))
        # return render(request, 'manager.html')
    emps = Employe.objects.all()
    manager = Employe.objects.filter(id= id)
    # data = serializers.serialize('json', Employe.objects.all())
    # print(data)
    leaves = Leaves.objects.filter(emp__manager = id).exclude(status ='Requested')
    pendingLeaves = Leaves.objects.filter(emp__manager = id, status='Requested')
    pd = serializers.serialize('json', pendingLeaves)
    request.session['pds']=pd;

    print('===============================')
    pprint.pprint(pd)
    return render(request, 'manager.html',
    {'emp': emps, 'manager': manager, 'leavs': leaves, 'email':request.session['useremail'], 'pds':pendingLeaves })

def newleave(request, id):
    print(request.method)
    print(request)
    if request.method== 'POST':
        emps = Employe.objects.get(id=id)
        print(request.POST['Input'])
        leav= Leaves(emp= emps, LEave_type= request.POST.get('Input'), status='Requested')
        leav.save()
        return HttpResponseRedirect('/OA/emp/'+str(id)+'/')
    return render(request, 'newleave.html')

def approval(request, id):
    # pprint(request.session['pds'])
    pprint.pprint(request.session['pds'])
    print(id)
    return render(request, 'approve.html', {'leave': id})
    return None