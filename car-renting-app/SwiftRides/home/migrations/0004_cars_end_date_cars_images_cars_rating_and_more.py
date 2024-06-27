# Generated by Django 5.0.1 on 2024-03-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_cars_user_information_delete_homes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='end_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='rating',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
