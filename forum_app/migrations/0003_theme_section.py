# Generated by Django 5.1.4 on 2024-12-15 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0002_message_message_author_message_related_theme_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='forum_app.section'),
        ),
    ]
