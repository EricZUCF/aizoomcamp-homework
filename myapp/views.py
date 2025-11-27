from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


def todo_list(request):
	todos = Todo.objects.order_by('resolved', 'due_date')
	return render(request, 'myapp/list.html', {'todos': todos})


def todo_create(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('myapp:todo_list')
	else:
		form = TodoForm()
	return render(request, 'myapp/form.html', {'form': form, 'title': 'Create Todo'})


def todo_edit(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	if request.method == 'POST':
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			form.save()
			return redirect('myapp:todo_list')
	else:
		form = TodoForm(instance=todo)
	return render(request, 'myapp/form.html', {'form': form, 'title': 'Edit Todo'})


def todo_delete(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	if request.method == 'POST':
		todo.delete()
		return redirect('myapp:todo_list')
	return render(request, 'myapp/confirm_delete.html', {'todo': todo})


def todo_toggle_resolved(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	todo.resolved = not todo.resolved
	todo.save()
	return redirect('myapp:todo_list')
