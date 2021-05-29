
from django.db import models

class News(models.Model):
    title = models.CharField('Заголовок', max_length=2000)
    description = models.TextField('Полное описание')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Добавить фото', null=True, blank=True, upload_to='news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

class Teacher(models.Model):
    photo = models.ImageField('Добавить фото', null=True, blank=True, upload_to='teachers')
    name = models.CharField('Ф.И.О', max_length=700, null=True, blank=True)
    position = models.TextField('Должность', max_length=5000, null=True, blank=True)
    edu = models.TextField('Образоание', max_length=500, null=True, blank=True)
    experience = models.TextField('Трудовая деятельность', max_length=5000, null=True, blank=True)
    certificates = models.TextField('Сертификаты', max_length=5000, null=True, blank=True)
    publications = models.TextField('Публикации', max_length=5000, null=True, blank=True)
    works = models.TextField('Основные работы', max_length=5000, null=True, blank=True)
    contacts = models.CharField('Контакты', max_length=1000, null=True, blank=True)

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

        