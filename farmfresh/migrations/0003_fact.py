# Generated by Django 4.1.3 on 2022-11-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmfresh', '0002_alter_aboutus_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
            ],
        ),
    ]