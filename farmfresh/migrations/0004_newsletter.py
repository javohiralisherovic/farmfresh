# Generated by Django 4.1.3 on 2022-11-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmfresh', '0003_fact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]
