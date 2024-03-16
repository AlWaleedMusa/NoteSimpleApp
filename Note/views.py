from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import add_noteForm
from django.db.models import Q


def main(request):
	notes = Notes.objects.all().order_by('-updated_at')

	context = {'notes': notes}
	return render(request, 'main.html', context)


def note(request, pk):
	show_lm = True

	note_data = get_object_or_404(Notes, id=pk)
	notes = Notes.objects.all().order_by('-updated_at')

	context = {'notes': notes, 'note_data': note_data, 'show_lm':show_lm}
	return render(request, 'main.html', context)


def add_note(request):
	notes = Notes.objects.all().order_by('-updated_at')
	add_note = True

	if request.method == 'POST':
		form = add_noteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ('add_note')
	else:
		form = add_noteForm()
		return render(request, 'main.html', {'form':form, 'add_note':add_note, 'notes':notes})
	

def delete_note(request, pk):
	note_to_delete = get_object_or_404(Notes, id=pk)
	note_to_delete.delete()
	return redirect('main')


def update_note(request, pk):
	notes = Notes.objects.all().order_by('-updated_at')
	show_update = True
	note_to_update = get_object_or_404(Notes, id=pk)

	if request.method == 'POST':
		form = add_noteForm(request.POST, instance=note_to_update)
		if form.is_valid():
			form.save()
			return redirect('main')
	else:
		form = add_noteForm(instance=note_to_update)
		return render(request, 'main.html', {'form':form, 'show_update':show_update, 'notes':notes})
	

def search(request):
	found = False
	note_to_find = None

	if request.method == 'POST':
		search_query = request.POST.get('search')

		note_to_find = Notes.objects.filter(
			Q(title__icontains=search_query) |
			Q(body__icontains=search_query)
		)

		if note_to_find:
			found = True

	return render(request, 'main.html', {'note_to_find':note_to_find, 'found':found})


def search_note(request, pk):
	search_note = True
	show_lm = True
	note_data = get_object_or_404(Notes, id=pk)

	context = {'note_data': note_data, 'search_note':search_note, 'show_lm':show_lm}
	return render(request, 'main.html', context)
