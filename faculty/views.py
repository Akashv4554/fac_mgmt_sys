from django.shortcuts import render
from .models import FacultyMember
from .fd import faculty_data
# Create your views here.


def faculty_home(request):
    fac=FacultyMember.objects.all()
    return render(request, 'view_fac.html',{'faculty':fac})

def faculty_detail(request, id):
    fac = FacultyMember.objects.get(id=id)
    return render(request, 'view_profile.html', {'faculty': fac})
