from django.shortcuts import render
from django.views import generic
from .models import Course

# Create your views here.

class CourseList(generic.ListView):
    queryset = Course.objects.filter(status=1)
    template_name = "index.html"
    paginate_by = 6
