# Generated by Django 4.2.3 on 2023-08-08 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_platform', '0004_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='lesson',
        ),
    ]
