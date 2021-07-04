from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Contacts, Students, Teacher, Feed, Achievements, Nomenklatura
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

def achievements(request):
    contacts = Contacts.objects.order_by('-id')
    achievements = Achievements.objects.order_by('-id')
    return render(request, 'main/achievements.html', {'headerTitle':'Наши достижения', 'achievements': achievements, 'contacts': contacts})

def shedule(request):
    contacts = Contacts.objects.order_by('-id')
    return render(request, 'main/shedule.html', {'headerTitle':'Расписания', 'contacts': contacts})

def about(request):
    contacts = Contacts.objects.order_by('-id')
    return render(request, 'main/about.html', {'headerTitle':'О кафедре', 'contacts': contacts})

def magistratura(request):
    contacts = Contacts.objects.order_by('-id')
    return render(request, 'main/magistratura.html', {'headerTitle':'Об учёбе', 'contacts': contacts})

def news(request):
    news = News.objects.order_by('-id')
    contacts = Contacts.objects.order_by('-id')
    return render(request, 'main/news.html', {'headerTitle':'Последние новости', 'news': news, 'contacts': contacts})

def newsDetail(request, pk):
    news = News.objects.filter(id=pk)
    contacts = Contacts.objects.order_by('-id')
    return render(request, 'main/news-details.html', {'headerTitle':'Подробнее о последних новостях', 'news': news, 'contacts': contacts})
    
def teachers(request, pk):
    teachers = Teacher.objects.filter(id=pk)
    contacts = Contacts.objects.order_by('-id')
    return render(request, 'main/teachers.html', {'title': 'Тороев Асылбек Абакирович', 'teachers': teachers, 'contacts': contacts})

def nomenklatura(request):
    nomenklatura = Nomenklatura.objects.order_by('-id')
    contacts = Contacts.objects.order_by('-id')
    return render(request, 'main/nomenklatura.html', {'headerTitle':'Номенклатура дел', 'nomenklatura': nomenklatura, 'contacts': contacts})
