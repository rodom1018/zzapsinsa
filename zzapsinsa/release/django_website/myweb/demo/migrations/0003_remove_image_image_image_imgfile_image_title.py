# Generated by Django 4.0.6 on 2022-08-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.TextField(max_length=40, null=True),
        ),
    ]
