from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=200, blank=True, null=True)
    named_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
