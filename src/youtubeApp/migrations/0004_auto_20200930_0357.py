# Generated by Django 3.1.1 on 2020-09-30 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeApp', '0003_auto_20200929_0943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='channnel_art',
            new_name='channel_art',
        ),
    ]