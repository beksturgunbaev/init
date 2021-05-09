
from django.db import models

class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    description = models.TextField('Полное описание')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Добавить фото', null=True, blank=True, upload_to='news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

class TeachersDetail(models.Model):
    photo = models.ImageField('Добавить фото', null=True, blank=True, upload_to='teachers')
    name = models.CharField('Ф.И.О', max_length=70)
    position = models.CharField('Должность', max_length=300)
    edu = models.CharField('Образоание', max_length=500)
    experience = models.TextField('Трудовая деятельность')
    certificates = models.CharField('Сертификаты', max_length=500)
    publications = models.TextField('Публикации')
    works = models.TextField('Основные работы')
    contacts = models.CharField('Контакты', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподваватель (подробнее)'
        verbose_name_plural = 'Преподаватели (подробнее)'

class Teacher(models.Model):
    photo = models.ImageField('Добавить фото', null=True, blank=True, upload_to='teachers')
    name = models.CharField('Ф.И.О', max_length=70)
    position = models.CharField('Должность', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподваватель'
        verbose_name_plural = 'Преподаватели'

class Students(models.Model):
    photo = models.ImageField('Добавить фото', null=True, blank=True, upload_to='students')
    name = models.CharField('Ф.И.О', max_length=150)
    position = models.CharField('Специальность', max_length=150)
    works = models.CharField('Работает в', max_length=140)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Выпускник'
        verbose_name_plural = 'Наши выпускники'

class Contacts(models.Model):
    phone = models.CharField('Телефон', max_length=70)
    phone2 = models.CharField('Доп. телефон', max_length=70)
    email = models.CharField('Почта', max_length=70)
    email2 = models.CharField('Доп. почта', max_length=70)
    adress = models.TextField('Адрес', max_length=140)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контакты'

class Feed(models.Model):
    feedName = models.CharField('Имя', max_length=70)
    feedPhone = models.CharField('Телефон', max_length=13)
    feedEmail = models.CharField('Почта', max_length=70)

    def __str__(self):
        return self.feedName

    class Meta:
        verbose_name = 'Заявка на обратный звонок'
        verbose_name_plural = 'Заявки на обратный звонок'