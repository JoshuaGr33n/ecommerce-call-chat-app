# Generated by Django 5.0.3 on 2024-03-05 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0002_admin_otp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin_otp',
            old_name='user',
            new_name='admin',
        ),
    ]
