from django.db import models

class GameListModel(models.Model):
    GENRE = (
        ('Экшн', 'Экшн'),
        ('Хоррор', 'Хоррор'),
        ('Аркада', 'Аркада')
    )
    title = models.CharField(max_length=100, verbose_name='Напишите название игры')
    image = models.ImageField(upload_to='games/', verbose_name='Добавьте фото')
    year = models.DateField(verbose_name='Укажите год выпуска')
    director = models.CharField(max_length=100, verbose_name='Укажите разработчика')
    genre = models.CharField(max_length=100, choices=GENRE)
    description = models.TextField(blank=True, verbose_name='Описание игры')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'игру'
        verbose_name_plural = 'Игры'


class Release(models.Model):
    game = models.CharField(max_length=100, verbose_name='Название релиза(игры)')

    part = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.game


class Slider(models.Model):
    slide = models.URLField()

    def __str__(self):
        return self.slide