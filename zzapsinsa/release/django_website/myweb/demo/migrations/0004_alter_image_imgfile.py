# Generated by Django 4.0.6 on 2022-08-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_remove_image_image_image_imgfile_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to='default/'),
        ),
    ]