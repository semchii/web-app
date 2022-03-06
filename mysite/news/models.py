from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100, unique=True, primary_key=True)
    bio = models.CharField(max_length=100)
    avatar = models.ImageField(blank=True, upload_to='user')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'


class Articles(models.Model):
    user = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True)
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Стаття')
    date = models.DateTimeField('Дата публікації')
    articles_img = models.ImageField(blank=True, upload_to='articles')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'


