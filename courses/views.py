from django.shortcuts import render, redirect
from .models import Teacher, Speciality, Subject
import random

# Create your views here.
def home_page(request):
    subjects = Subject.objects.all().order_by('-created_at')[:5]
    teachers= Teacher.objects.all().order_by('-created_at')[:5]
    specialities = Speciality.objects.all().order_by('-created_at')[:5]

    context = {
        'subjects':subjects,
        'specialities':specialities,
        'teachers': teachers
    }

    return render (request, 'home.html', context = context)


def teacher_detail(request, id):
    teacher = Teacher.objects.get(id=id)
    context = {
        'teacher': teacher
    }
    return render(request, 'teacher_detail.html', context= context)


def speciality_detail(request, id):
    speciality = Speciality.objects.get(id=id)
    context = {
        'speciality': speciality
    }
    return render(request, 'speciality_detail.html', context= context)

def speciality_create(request):
    if request.method == "Post":
        name= request.Post['name']
        date= request.Post['date']
        is_active= True if request.Post['is_active']=='on' else False
        Speciality.objects.create(name=name, start_date=date, is_active=is_active)
        return redirect('home-page')
    else:
        return render (request, 'speciality_create.html')
    
def teacher_create(request):
    if request.method == "Post":
        first_name= request.Post['first_name']
        last_name= request.Post['last_name']
        degree= request.Post['Degree']
        age= request.Post('age')
        Teacher.objects.create(first_name=first_name, last_name= last_name, degree = degree, age=age)
        return redirect('home-page')
    else:
        return render (request, 'teacher_create.html')
    
    #  Degree = [
    #     ( "master", "Master"),
    #     ("bachelor", "Bachelor"),
    #     ("academic", "Academic"),
    #     ("drscience", "DrScience"),
    #     ("phs", "PhD"),
    # ]

    # first_name = models.CharField(max_length=28)
    # last_name = models.CharField(max_length=28)
    # degree = models.CharField(max_length=9, choices=Degree)
    # age = models.IntegerField()
    # email = models.EmailField(unique=True)
