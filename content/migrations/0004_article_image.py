# Generated by Django 5.2.1 on 2025-06-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_article_options_article_is_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/', verbose_name='Image'),
        ),
    ]
