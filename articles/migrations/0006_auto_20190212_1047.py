# Generated by Django 2.1.6 on 2019-02-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_has_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='has_answer',
            field=models.BooleanField(default=True),
        ),
    ]