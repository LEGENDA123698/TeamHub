# Generated by Django 5.1.4 on 2024-12-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_survey_app', '0004_alter_freecomment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='comments_media/'),
        ),
        migrations.DeleteModel(
            name='FreeComment',
        ),
    ]
