from django.db import models

class FeedBack(models.Model):
    name = models.CharField('Имя', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    email = models.CharField('E-mail', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Форма обратной связи'
