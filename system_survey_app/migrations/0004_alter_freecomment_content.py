# Generated by Django 5.1.4 on 2024-12-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_survey_app', '0003_survey_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecomment',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
