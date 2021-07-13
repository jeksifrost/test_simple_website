from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=50, default='')
    announcement = models.CharField('Announcement', max_length=250, default='')
    full_text = models.TextField('Article')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
