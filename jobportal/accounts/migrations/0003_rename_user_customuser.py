# Generated by Django 4.1.4 on 2023-03-05 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('accounts', '0002_rename_customuser_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
