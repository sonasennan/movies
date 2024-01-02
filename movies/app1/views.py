from django.shortcuts import render
from app1.models import Movie
from app1.forms import MovieForm
# app_name="app1"

# Create your views here.
def home(request):
    b=Movie.objects.all()
    return render(request,'home.html',{'movie':b})

def view(request,p):
    b=Movie.objects.get(id=p)
    return render(request, 'view.html',{'b': b})

def editmovie(request,p):
    b=Movie.objects.get(id=p)
    if(request.method=="POST"):
        form=MovieForm(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return view(request,p)
    form=MovieForm(instance=b)
    return render(request,'editmovie.html',{'f':form})

def deletemovie(request,p):
    b=Movie.objects.get(id=p)
    if(request.method=="POST"):
        b.delete()
        return home(request)
    return render(request, 'del.html')


def addmovie(request):
    if(request.method=="POST"):
        i=request.FILES['i']
        t=request.POST['t']
        d=request.POST['d']
        b=Movie.objects.create(image=i,title=t,description=d)
        b.save()
        return home(request)
    return render(request,'addmovies.html')



