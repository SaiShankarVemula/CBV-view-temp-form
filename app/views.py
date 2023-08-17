from typing import Any, Dict  ### it is used for 
from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *
from django.views.generic import View,TemplateView,FormView


# Create your views here.

def Sf(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    return render(request,'Sf.html',d)

class Temprenderdata(TemplateView):
    template_name='Temprenderdata.html'   
    def get_context_data(self, **kwargs):  # it will inherit the properties from the TemplateView parent
        ECDO=super().get_context_data(**kwargs) ## here we r performing super() chaining and it will create and return Empty Context Object and then we storing the data into one variable
        SFO=StudentForm()
        ECDO['SFO']=SFO
        return ECDO
    
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('DataInserted')
        
 ## The above Temprenderdata class we never use bcz its lengthy compared to FormView

class StuFormInsertData(FormView):
    template_name='StuFormInsertData.html'
    form_class=StudentForm
    
    def form_valid(self, form):
        form.save()
        return HttpResponse('Data Inserted Successfully')