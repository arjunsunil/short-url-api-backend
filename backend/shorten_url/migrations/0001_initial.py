# Generated by Django 4.1.2 on 2022-10-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('short_url', models.URLField(blank=True, max_length=50, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]