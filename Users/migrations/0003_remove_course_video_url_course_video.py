# Generated by Django 4.2.9 on 2024-02-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_course_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='video_url',
        ),
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
