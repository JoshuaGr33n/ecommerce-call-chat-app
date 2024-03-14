# Generated by Django 5.0.3 on 2024-03-06 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_custom_user_deleted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userotp',
            name='otp_type',
            field=models.CharField(blank=True, choices=[('Password', 'Password'), ('Login', 'Login')], default='Login', max_length=50, null=True),
        ),
    ]
