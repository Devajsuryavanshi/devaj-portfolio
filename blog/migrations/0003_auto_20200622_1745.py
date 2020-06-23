# Generated by Django 3.0.7 on 2020-06-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='descriprion',
            new_name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
