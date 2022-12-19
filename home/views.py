from django.shortcuts import render, redirect
from .forms import AppForm, planForm, SubsForm
from .models import App, Plans, Subscription

# home render page
def home(request):
    packages = [
        {'name': 'App', 'url': 'app/show'},
        {'name': 'Plans', 'url': 'plans'},
        {'name': 'Subs', 'url': 'subs'},
    ]
    context = {
        'packages': packages
    }
    return render(request, 'home/index.html', context)

# app render page
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
    return render(request, 'index.html', {'form': form,'nbar':'app'})

# list of apps page
def show(request):
    apps = App.objects.all()

    return render(request, "show.html", {'apps': apps,'nbar':'app'})

# edit of apps page
def edit(request, id):
    app = App.objects.get(id=id)
    return render(request, 'edit.html', {'app': app,'nbar':'app'})

# edit apps api
def update(request, id):
    app = App.objects.get(id=id)
    form = AppForm(request.POST, instance=app)
    if form.is_valid():
        form.save()
        return redirect("/app/show")
    return render(request, 'edit.html', {'app': app,'nbar':'app'})

# delete apps api
def destroy(request, id):
    app = App.objects.get(id=id)
    app.delete()
    return redirect("/app/show")


# show plans page render
def plans(request):
    plans = Plans.objects.all()

    return render(request, "plans/show.html", {'plans': plans,'nbar':'plan'})


#not needed, used to add the 3 plans
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
    return render(request, 'plans/plan.html', {'form': form,'nbar':'plan'})

#render list of subs
def subs(request):
    subs = Subscription.objects.all()

    return render(request, "Subs/show.html", {'subs': subs,'nbar':'subs'})

#render sub form page
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
    return render(request, 'Subs/add.html', {'form': form,'nbar':'subs'})

#render sub edit form page
def editSubs(request, id):
    sub = Subscription.objects.get(id=id)
    apps = App.objects.all()
    return render(request, 'Subs/edit.html', {'sub': sub, 'apps': apps,'nbar':'subs'})

#update subs api call
def updateSubs(request, id):
    sub = Subscription.objects.get(id=id)
    apps = App.objects.all()
    form = SubsForm(request.POST, instance=sub)
    if form.is_valid():
        form.save()
        return redirect("/subs")
    return render(request, 'Subs/edit.html', {'sub': sub, 'apps': apps,'nbar':'subs'})
