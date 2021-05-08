from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Contacts, Students, Teacher, TeachersDetail

def index(request):
    teacher = Teacher.objects.order_by('-id')
    student = Students.objects.order_by('-id')
    contacts = Contacts.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Институт Новых Информационных Технологий', 'teacher': teacher, 'student': student, 'contacts': contacts})

def news(request):
    news = News.objects.order_by('-id')[:8]
    return render(request, 'main/news.html', {'headerTitle':'Последние новости', 'news': news})
    
def teachers(request):
    teachers = TeachersDetail.objects.order_by('-id')
    return render(request, 'main/teachers.html', {'title': 'Тороев Асылбек Абакирович', 'teachers': teachers})


