# Generated by Django 3.2.16 on 2024-04-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_maintenance'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitepreferences',
            name='login_help_text',
            field=models.TextField(default='', help_text='Help text to show in login page.'),
        ),
    ]
