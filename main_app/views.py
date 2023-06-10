from django.shortcuts import redirect, render
from main_app.models import TODO,Person
from django.contrib.auth.decorators import login_required
from main_app.forms import PersonForm
# Create your views here.
def home(request):
    todo=TODO.objects.all()
    return render(request,'main_app/home.html',{'todo':todo})


@login_required
def add(request):
    if request.method=='GET':
        return render(request,'main_app/add-todo.html')
    else:
        title=request.POST['title']
        desc=request.POST['desc']

        TODO.objects.create(title=title,description=desc,is_completed=False, user_id=request.user.id)

        return redirect('main_app-home')

@login_required
def delete(request,id):
    TODO.objects.get(id=id).delete()
    return redirect('main_app-home')    


@login_required
def edit(request,id):
    try:
     todo=TODO.objects.get(id=id)
    except:
        return redirect('main_app-404')   
    if request.method=='GET':
        return render(request,'main_app/edit-todo.html',{'todo':todo})
    else:
        title=request.POST['title']
        desc=request.POST['desc']

        todo.title=request.POST['title']
        todo.description=request.POST['desc']
        todo.save()
        return redirect('main_app-home')

@login_required
def delete_all(request):
    try:
     TODO.objects.all().delete() 
    except:
       return redirect('main_app-404')
    return redirect('main_app-home')

@login_required
def markcomplete(request,id):
    try:
     todo=TODO.objects.get(id=id)
    except:
       return redirect('main_app-404')
    if todo.is_completed:
     todo.is_completed=False
    else:
        todo.is_completed=True
        todo.save()
    return redirect('main_app-home')   


def not_found(request):
    return render(request,'core/404.html')




# def person(request):
#    if request.method=='GET':
#       form=PersonForm()  #form class ko instance created
#       return render(request,'main_app/person.html',{'form':form})
#    else:
#       form=PersonForm(request.POST)
#       if form.is_valid():
#         form.save()
           
        #  fn=form.cleaned_data['first_name']
        #  ln=form.cleaned_data['last_name']
        #  age=form.cleaned_data['age']
        #  email=form.cleaned_data['email']
        #  password=form.cleaned_data['password']

        #  Person.objects.create(first_name=fn,last_name=ln,age=age,email=email,password=password)

        
        # return redirect('main_app-home')