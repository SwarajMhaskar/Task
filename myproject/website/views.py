from django.shortcuts import render
from .models import Emp

def home(request):
    all_emp = Emp.objects.all()
    return render(request, 'home.html', {'all_emp': all_emp})

def search_view(request):
    query = request.GET.get('query')
    results = Emp.objects.filter(id=query)
    return render(request, 'search_results.html', {'results': results})

