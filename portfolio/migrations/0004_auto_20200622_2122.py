# Generated by Django 3.0.7 on 2020-06-22 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200620_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descriprion',
            new_name='description',
        ),
    ]
