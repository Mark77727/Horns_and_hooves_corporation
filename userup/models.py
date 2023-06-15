from django.db import models


class portfolio(models.Model):
    name = models.TextField(verbose_name="Название")
    content = models.TextField(verbose_name="Описание")
    cover = models.ImageField(upload_to="images/")
    urls_path = models.URLField()

    def __str__(self):
        return self.name
