# Generated by Django 4.2.3 on 2023-08-12 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='site_logo',
            field=models.FileField(upload_to='site-settings', verbose_name='لوگو سایت'),
        ),
    ]
