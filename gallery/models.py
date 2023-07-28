from django.db import models


class Image(models.Model):
    img_name = models.CharField(max_length=50)
    img_file = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.img_name
