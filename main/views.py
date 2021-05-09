from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Contacts, Students, Teacher, TeachersDetail, Feed
from .forms import feedForm

def index(request):
    error = ''
    if request.method == 'POST':
        form = feedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма было неверной!'

    form = feedForm()
    
    teacher = Teacher.objects.order_by('-id')
    student = Students.objects.order_by('-id')
    contacts = Contacts.objects.order_by('-id')
    return render(request, 'main/index.html', {'form': form, 'title': 'Институт Новых Информационных Технологий', 'teacher': teacher, 'student': student, 'contacts': contacts})

def news(request):
    news = News.objects.order_by('-id')[:8]
    return render(request, 'main/news.html', {'headerTitle':'Последние новости', 'news': news})
    
def teachers(request):
    teachers = TeachersDetail.objects.order_by('-id')
    return render(request, 'main/teachers.html', {'title': 'Тороев Асылбек Абакирович', 'teachers': teachers})


