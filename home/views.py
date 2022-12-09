from django.shortcuts import render,redirect
from .forms import AppForm ,planForm ,SubsForm
from .models import App ,Plans,Subscription



def home(request):
    packages = [
	{'name':'App', 'url': 'app/show'},
	{'name':'Plans', 'url': 'plans'},
	{'name':'Subs', 'url': 'subs'},
    ]
    context = {
        'packages': packages
    }
    return render(request, 'home/index.html', context)

def app(request):  
    if request.method == "POST":  
        form = AppForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/app/show')  
            except:  
                pass  
    else:  
        form = AppForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    apps = App.objects.all() 
   
    return render(request,"show.html",{'apps':apps})  
def edit(request, id):  
    app = App.objects.get(id=id)  
    return render(request,'edit.html', {'app':app})  

def update(request, id):  
    app = App.objects.get(id=id)  
    form = AppForm(request.POST, instance = app)  
    if form.is_valid():  
        form.save()  
        return redirect("/app/show")  
    return render(request, 'edit.html', {'app': app})  

def destroy(request, id):  
    app = App.objects.get(id=id)  
    app.delete()  
    return redirect("/app/show")  

def plans(request):  
    plans = Plans.objects.all() 
   
    return render(request,"plans/show.html",{'plans':plans}) 

def plan(request):  
    if request.method == "POST":  
        form = planForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('plans/plan.html')  
            except:  
                pass  
    else:  
        form = planForm()  
    return render(request,'plans/plan.html',{'form':form}) 

def subs(request):  
    subs = Subscription.objects.all() 
   
    return render(request,"Subs/show.html",{'subs':subs})

def addSubs(request):  
    if request.method == "POST":  
        form = SubsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/subs')  
            except:  
                pass  
    else:  
        form = SubsForm()  
    return render(request,'Subs/add.html',{'form':form}) 

def editSubs(request, id):  
    sub = Subscription.objects.get(id=id)
    apps = App.objects.all() 
    return render(request,'Subs/edit.html', {'sub':sub,'apps':apps}) 

def updateSubs(request, id):  
    sub = Subscription.objects.get(id=id)
    apps = App.objects.all() 
    form = SubsForm(request.POST, instance = sub)  
    if form.is_valid():  
        form.save()  
        return redirect("/subs")  
    return render(request,'Subs/edit.html', {'sub':sub,'apps':apps}) 