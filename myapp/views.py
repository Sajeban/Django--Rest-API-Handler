import datetime

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from myapp.forms import  ContactForm
import pymongo

client = pymongo.MongoClient("mongodb+srv://Sajeban:Monkey-1002@homelook-pdmeg.gcp.mongodb.net/test?retryWrites=true",ssl=True)
#client = pymongo.MongoClient("mongodb://Sajeban:Monekey-1002@homelook-shard-00-00-pdmeg.gcp.mongodb.net:27017,homelook-shard-00-01-pdmeg.gcp.mongodb.net:27017,homelook-shard-00-02-pdmeg.gcp.mongodb.net:27017/test?ssl=true&replicaSet=HomeLook-shard-0&authSource=admin&retryWrites=true")
print(client)
m_db = client.get_database('Users')
print(m_db)
m_collection = m_db.Staff

#def hello(request):
 #  return render(request, "hello.html", {})
def hello(request, number):
   see(number)
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)

def greet(request):
   today = datetime.datetime.now().date()
   return render(request, "hello.html", {"today" : today})



def login(request):
    return render(request, "login.html")
def see(x):

    newstaff = {
    'name': x,
        'Email' : 'Tvia@gmail.com'
    }
    m_collection.insert_one(newstaff)
    list1 = (m_collection.find())


def register(request):
    if(request.method=='POST'):
        form   = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponse("Success")
    else:
        form  = UserCreationForm()
        args={'form':form}
        return render(request,'reg_form.html',args)

def register2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data
            print(text)
            m_collection.insert_one(text)
            return render(request, 'reg2.html', {'form': form,'text':text})
    else:
        form = ContactForm()
        return render(request, 'reg2.html', {'form': form})

