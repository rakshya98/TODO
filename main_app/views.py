from django.shortcuts import redirect, render
from main_app.models import TODO
from django.contrib.auth.decorators import login_required

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