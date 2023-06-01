from django.shortcuts import redirect, render
from main_app.models import TODO


# Create your views here.
def home(request):
    todo=TODO.objects.all()
    return render(request,'main_app/home.html',{'todo':todo})

def add(request):
    if request.method=='GET':
        return render(request,'main_app/add-todo.html')
    else:
        title=request.POST['title']
        desc=request.POST['desc']

        TODO.objects.create(title=title,description=desc,is_completed=False, user_id=1)

        return redirect('main_app-home')


def delete(request,id):
    TODO.objects.get(id=id).delete()
    return redirect('main_app-home')                       

def edit(request,id):
    todo=TODO.objects.get(id=id)
    if request.method=='GET':
        return render(request,'main_app/edit-todo.html',{'todo':todo})
    else:
        title=request.POST['title']
        desc=request.POST['desc']

        todo.title=request.POST['title']
        todo.description=request.POST['desc']
        todo.save()
        return redirect('main_app-home')


def delete_all(request):
    
    TODO.objects.all().delete() 
    return redirect('main_app-home')