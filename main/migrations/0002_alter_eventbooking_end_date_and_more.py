# Generated by Django 4.0 on 2022-01-09 17:46

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventbooking',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='eventbooking',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.get_image_filename),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='yacht',
            name='rate',
            field=models.IntegerField(),
        ),
    ]
