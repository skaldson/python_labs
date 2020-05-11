# Generated by Django 3.0.5 on 2020-05-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file_catalog', '0003_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='books/img')),
            ],
        ),
    ]
