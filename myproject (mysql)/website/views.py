from django.shortcuts import render
from .models import Employee

def home(request):
    all_emp = Employee.objects.all()
    return render(request, 'home.html', {'all_emp': all_emp})

def search_view(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if not query:
            return render(request, 'search_results.html', {'error': 'Please enter the ID.'})
        results = Employee.objects.filter(id=query)
        return render(request, 'search_results.html', {'results': results})


def get_employees():
    employees = Employee.objects.all()
    return employees
