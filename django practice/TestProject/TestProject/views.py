from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import UserForm
from service.models import Service
from person.models import Person
from saveformdata.models import SaveFormData



def HomePage(request):
    ServiceData = Service.objects.all().order_by('Name') # for desending order '-Name' i.e "-" is included
    # slicing can be used as regular slicng in list but negative indexing is not used
    PersonData = Person.objects.all().order_by('person_name')

    if request.method=="GET":
        search = request.GET.get('search')
        if search!=None:
            ServiceData = Service.objects.filter(Name__icontains=search) # For partial match, i.e even single letter matches , it shows
            # ServiceData = Service.objects.filter(Name=search)  To make Exact match and search
    data={
        'ServiceData':ServiceData,
        'PersonData':PersonData
    }
    return render(request,"index.html",data)

def SaveData(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        website=request.POST.get('website')
        message=request.POST.get('message')
    s = SaveFormData(Name=name,Email=email,Website=website,Message=message)
    s.save()
    n="Data saved Successfully ✅"
    return render(request,'index.html',{"con":n})


def PersonDetail(request,personid):
    personDetail = Person.objects.get(id=personid)
    data={
        'PersonDetail':personDetail
    }
    return render(request,'persondetail.html',data)
def aboutUS(request):
    return render(request,"about.html")
def course(request):
    return HttpResponse("This course page")
def courseDetail(request,courseid):
    return HttpResponse(courseid)

def userForm(request):
    total =0
    try:
        #n1 = int(request.GET['num1'])
        #n2 = int(request.GET['num2'])
        #
        #       Or you can also write it as
        n1 = int(request.GET.get('num1'))
        n2 = int(request.GET.get('num2'))
        total = n1+n2
    except:
        pass
    return render(request,'userform.html',{'Output':total})

def secureUserForm(request):
    total_num=0
    django_form = UserForm()
    data1={'form':django_form}
    try:
        nu1=int(request.POST.get('n1'))
        nu2=int(request.POST.get('n2'))
        total_num=nu1+nu2
        data1={
                'form':django_form,
                'output':total_num
            }
        url = "/success/?output={}".format(total_num)

        #return redirect(url)
        # or 
        return HttpResponseRedirect(url)

    except:
        pass
    return render(request,'secureuserform.html',data1)

def success(request):
    output = request.GET.get('output')
    return render(request,'thankyou.html',{'output':output})

def Calculator(request):
    answer=''
    data={}
    try:
        n1=eval(request.POST.get('num1'))
        n2=eval(request.POST.get('num2'))
        opr=request.POST.get('operation')
        if opr=='+':
            answer=n1+n2
        elif opr=='-':
            answer = n1-n2
        elif opr=='*':
            answer = n1*n2
        elif opr=='/':
            answer = n1/n2
        data={'answer':answer}
    except:
        answer="Invalid Operation"
        data={'answer':answer}        
        
    return render(request,'calculator.html',data)

def EvenOdd(request):
    message=''
    try:
        n=int(request.POST.get('num1'))
        if n%2==0:
            message='Even Number'
        else:
            message='Odd Number'
    except:
        pass
    return render(request,'evenodd.html',{'message':message})