from django.shortcuts import render
from django.http import HttpResponse
from testapp.mixins import HttpResponseMixins



#httpresponse
# Create your views here.

import json
def emp_data_view(request):
    emp_data={
        "eno":101,
        "ename":"kanchan",
        "esal":30000,
        "eaddr":"pune"

    }

    resp="<h1>Employee number:{}<br> Employee Name:{}<br> Employee sallary:{}<br> Employee Address:{}</h1>".format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

#repsonse in json formate
def emp_json_view(request):
    emp_data={
        'eno':101,
        'ename':"kanchan",
        "esal":30000,
        "eaddr":"pune"

    }
    json_data=json.dumps(emp_data)#converting python object to json by using dumps
    return HttpResponse(json_data,content_type='application/json')


#we can send json response also in another way
from django.http import JsonResponse
def json_view(request):
    emp_data={
        'eno':101,
        'ename':"kanchan",
        "esal":30000,
        "eaddr":"pune"
    }
    return JsonResponse(emp_data)


#classbase view(CBV)
from django.views.generic import View
from testapp.mixins import HttpResponseMixins

class JsonCBV(HttpResponseMixins,View):
    def get(self,request,*args,**kwargs,):
        json_data=json.dumps({'msg':'this is from get method'})
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs,):
        json_data=json.dumps({'msg':'this is from post method'})
        return self.render_to_http_response(json_data)

    def put(self,request,*args,**kwargs,):
        json_data=json.dumps({'msg':'this is from put method'})
        return self.render_to_http_respons(json_data)

    def delete(self,request,*args,**kwargs,):
        json_data=json.dumps({'msg':'this is from delete method'})
        return self.render_to_http_response(json_data)



