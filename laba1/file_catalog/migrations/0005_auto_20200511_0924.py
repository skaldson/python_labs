# Generated by Django 3.0.5 on 2020-05-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_catalog', '0004_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='book',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='my_file',
            field=models.FileField(default=0, upload_to='files'),
            preserve_default=False,
        ),
    ]
