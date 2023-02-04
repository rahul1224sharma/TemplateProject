from django.shortcuts import render

# Create your views here.
def f1(request):
    return render(request,'MyApps1/child.html')


def f2(request):
    return render(request,'MyApps1/child1.html')

def demo1(request):
    dict1={'msg1':'RAHUL KUMAR SHARMA','msg2':'rahul kumar sharma','msg3':'Hi','msg4': 'mohit kumar sharma','msg5':'filters success'}
    return render(request,'MyApps1/demo1.html',context=dict1)

import datetime;
def demo2(request):
    date1=datetime.datetime.now()
    dict1={'name':'rahulkumarsharma','subject':'MCA','dept':'Computer Application','date1':date1}
    return render(request,'MyApps1/demo2.html',context=dict1)
def demo3(request):
    return render(request,'MyApps1/demo3.html')
def thankyou(request):
    dict1={'v1':v1,'v2':v2}
    return render(request,'MyApps1/thankyou.html',context=dict1)