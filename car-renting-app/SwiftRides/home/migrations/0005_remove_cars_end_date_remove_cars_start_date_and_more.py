# Generated by Django 5.0.1 on 2024-03-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cars_end_date_cars_images_cars_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='user_information',
            name='surname',
        ),
        migrations.AddField(
            model_name='user_information',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
