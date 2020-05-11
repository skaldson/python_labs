from django.db import models


class File(models.Model):
    description = models.CharField(max_length=100, blank=True)
    my_file = models.FileField(upload_to='files')
    file_list = list()

    def __str__(self):
        return self.description
