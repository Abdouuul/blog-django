# Generated by Django 5.2.1 on 2025-06-05 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Avatar'),
        ),
    ]
