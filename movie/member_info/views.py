from django.shortcuts import render, Http404,HttpResponse,HttpResponseRedirect
from member_info.models import NuomiMovie
# Create your views here.


def index(request):
    obj = NuomiMovie.objects.all()
    # for i in obj:
    #     print(i.zhuyao)
    return render(request, 'index.html', {'obj':obj,})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

