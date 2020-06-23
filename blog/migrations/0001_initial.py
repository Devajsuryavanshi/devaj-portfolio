# Generated by Django 3.0.7 on 2020-06-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descriprion', models.TextField()),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='blog_image')),
            ],
        ),
    ]
