from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):

    CHOICES = (
        ('Запланировано', 'Запланировано'),
        ('Изменено', 'Изменено'),
        ('Отменено', 'Отмененно'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=300, choices = CHOICES, blank=False, default='Отправлено')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    