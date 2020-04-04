from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404
# Create your views here.

def project_list(request):
    return render(request, 'budget/project-list.html')

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render(request, 'budget/project-detail.html', {'project': project,
                                                          'expense_list': project.expenses.all()})


