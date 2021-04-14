from django.shortcuts import render,redirect
from api.models import Account
from .serializers import AccountSerialiser
import json
from django.http import HttpResponse,JsonResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.

def index(request):
    obj = Account.objects.all()
    data = { "result" :list(obj.values())
            }
    return JsonResponse(data)

def create(request):
     if(request.method == 'GET'):
            return render(request , 'api/apicreate.html')
     if(request.method == 'POST'):
                myfile = request.FILES['image']
                fs = FileSystemStorage('./api/static/api')
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                urlimage = '/static/api/' + uploaded_file_url
                datacoopy = request.POST.copy()
                datacoopy['image'] = urlimage
                serializer = AccountSerialiser(data=datacoopy)
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
                myfile = request.FILES['image']
                fs = FileSystemStorage('./api/static/api')
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                urlimage = '/static/api/' + uploaded_file_url
                datacopy = request.POST.copy()
                datacopy['image'] = urlimage
                serializer = AccountSerialiser(instance=obj , data=datacopy)
                if serializer.is_valid():
                        serializer.save()
                return redirect('/') 