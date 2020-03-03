from django.shortcuts import render
import datetime
def home(request):
    return  render(request , 'base.html')
# Create your views here.
def other(request):
    context= {
    'k1' : 'Welcome to the second page',
    }
    return render(request, 'other.html', context)

def about(request):
    time = datetime.datetime.now()
    return render(request,'about.html',{'time' : time})