# Generated by Django 4.2.1 on 2023-05-19 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='descpn',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='pic',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='team_name',
            new_name='name',
        ),
    ]
