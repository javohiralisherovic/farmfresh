# Generated by Django 4.1.3 on 2022-11-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmfresh', '0009_aboutus_facebook_url_aboutus_instagram_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mobile_images'),
        ),
        migrations.AddField(
            model_name='feature',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mobile_images'),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mobile_images'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='feature',
            name='description_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='description_uz',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_uz',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
