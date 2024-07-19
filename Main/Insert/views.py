from django.shortcuts import render, redirect
from .models import Insert
from .forms import InsertForm
from django.shortcuts import get_object_or_404

def insert_list(request):
    inserts = Insert.objects.order_by('-no')[:50] 
    return render(request, 'insert_list.html', {'inserts': inserts})

def add_insert(request):
    if request.method == 'POST':
        form = InsertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insert_list')
    else:
        form = InsertForm()
    return render(request, 'edit_insert.html', {'form': form})


def edit_insert(request, pk):
    insert = get_object_or_404(Insert, pk=pk)
    if request.method == 'POST':
        form = InsertForm(request.POST, instance=insert)
        if form.is_valid():
            form.save()
            return redirect('insert_list')
    else:
        form = InsertForm(instance=insert)
    return render(request, 'edit_insert.html', {'form': form, 'insert': insert})


def delete_insert(request, pk):
    insert = get_object_or_404(Insert, pk=pk)
    if request.method == 'POST':
        insert.delete()
        return redirect('insert_list')
    return render(request, 'confirm_delete.html', {'insert': insert})

