from django.shortcuts import render, redirect
from .models import TableRow
from .forms import TableRowForm

def display_table(request):
    rows = TableRow.objects.order_by('emp_id')
    return render(request, 'table.html', {'rows': rows})

def display_selected_row(request, row_id):
    try:
        selected_row = TableRow.objects.get(pk=row_id)
    except TableRow.DoesNotExist:
        selected_row = None
    return render(request, 'selected_row.html', {'selected_row': selected_row})

def add_row(request):
    if request.method == 'POST':
        form = TableRowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_table')
    else:
        form = TableRowForm()

    return render(request, 'add_row.html', {'form': form})