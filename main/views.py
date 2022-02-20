from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import InsertForm,MarkForm
from .models import Mark,Personal

# Create your views here.



def home(request):
    return render(request,"home.html",context={})



def insert(request):
    if request.method == "POST":
        form = InsertForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks for filling your details ,now go back/refresh the page and please fill your makrks")
    else:
        form = InsertForm()
    return render(request, "insert.html", context={"form": form})

def mark(request):
    if request.method == "POST":
        form = MarkForm(request.POST)
        if form.is_valid():
             obj=form.save(commit=False)
             dic=request.POST
             m1=int(dic.get("m1"))
             m2=int(dic.get("m2"))
             m3=int(dic.get("m3"))
             m4=int(dic.get("m4"))
             m5=int(dic.get("m5"))
             obj.total=int(m1+m2+m3+m4+m5)
             obj.save()
             dis=Mark.objects.all()
             return render(request,"display.html",{"dis": Mark.objects.all().order_by('-total'),"mark":Mark.objects.all()})
    
    else:
        form = MarkForm()
    return render(request, "mark.html", context={"form": form})




def display(request):
     return render(request,"display.html",{"dis": Mark.objects.all().order_by('-total'),"mark":Mark.objects.all()})



