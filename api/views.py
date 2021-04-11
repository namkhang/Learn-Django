from django.shortcuts import render,redirect
from api.models import Account
from .serializers import AccountSerialiser
import json
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    obj = Account.objects.all()
    print(obj)
    data = { "result" :list(obj.values("id", "username", "password", "fullname"))
            }
    return JsonResponse(data)

def create(request):
     if(request.method == 'GET'):
            return render(request , 'api/apicreate.html')
     if(request.method == 'POST'):
            serializer = AccountSerialiser(data=request.POST)
            if serializer.is_valid():
                    serializer.save()
            return redirect('/')


def getdata(requet , id):
        iduser = int(id)
        obj = Account.objects.get(id=iduser)
        data =AccountSerialiser(obj,many=False)
        return JsonResponse(data.data)


def deletedata(request , id):
        if request.method == 'GET':
                iduser = int(id)
                obj = Account.objects.get(id=iduser)
                obj.delete()
                return redirect('/')
      

def updatedata(request):
        if request.method == 'GET':
                return render(request , 'api/apiupdate.html')
        if request.method == 'POST':
                iduser = int(request.POST['id'])
                obj = Account.objects.get(id=iduser)
                serializer = AccountSerialiser(instance=obj , data=request.POST)
                if serializer.is_valid():
                        serializer.save()
                return redirect('/')  