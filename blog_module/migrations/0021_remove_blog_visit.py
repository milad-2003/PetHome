# Generated by Django 4.2.3 on 2023-08-22 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0020_blog_visit_alter_blogvisit_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='visit',
        ),
    ]
