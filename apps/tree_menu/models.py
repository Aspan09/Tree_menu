from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название меню")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name="Меню")
    name = models.CharField(max_length=100, verbose_name="Название пункта меню")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children', verbose_name="Родительский пункт")
    url = models.CharField(max_length=255, blank=True, verbose_name="URL или named URL")
    named_url = models.CharField(max_length=100, blank=True, verbose_name="Named URL")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        unique_together = ('menu', 'name')
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url
