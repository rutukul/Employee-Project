from django.shortcuts import render
from .models import employee
# Create your views here.
def home(request):
    if request.method == 'POST':
        if request.POST['button']=="sb":
            info2 = request.POST['textbar']
            print(info2)    
            info3 = employee.objects.filter(first_name__icontains = info2 )|employee.objects.filter(last_name__icontains =info2)
            print(info3)
            return render(request,"home.html",{'info':info3})
        else:
            info1 = request.POST['button']
            print(info1) 
            info = employee.objects.get(pk = info1)
            return render(request,"info.html",{'info':info})
    else:
        info = employee.objects.all()
        return render(request, "home.html",{'info':info})