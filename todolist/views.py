from django.shortcuts import render , get_object_or_404 , redirect
from .models import Todo
from .forms import TodoPost

def home(request):
    return render(request, 'home.html')

def todo(request):
    todos = Todo.objects
    return render(request, 'todo.html', {'todos': todos})

def create(request):
    if (request.method == 'POST'):
        form = TodoPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user= current user()
            post.save()
            return redirect('todo')
    else:
        form = TodoPost()
        return render(request, 'new.html', {'form':form})

def edit(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    
    if (request.method == 'POST'):
        todo.item = request.POST['item']
        #todo.user = current user
        todo.save()
        return redirect('todo')
    
    return render(request,'edit.html', {'todo':todo} )

def destroy(request, todo_id ):
    todo = Todo.objects.get(pk = todo_id)
    todo.delete()
    return redirect('todo')