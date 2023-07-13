from django.shortcuts import render
from .models import Place, Team
# Create your views here.
from django .http import HttpResponse
def demo(request):
    obj=Place.objects.all()
    res=Team.objects.all()
    #name="india"
    return render(request,"index.html",{'result':obj,'result1':res})
#def operations(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #add=x+y
    #sub=x-y
    #mul=x*y
    #div=x/y
    #return render(request,"result.html",{"res":add,"resu":sub,"resul":mul,"result":div,"number1":x,"number2":y})

#def about(request):
   # return render(request,"page.html")
#def contact(request):
   # return render(request,"new.html")
#def detail(request):
    #return HttpResponse("detail")
#def thanks(request):
    #return render(request,"last.html")