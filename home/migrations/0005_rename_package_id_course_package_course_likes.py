# Generated by Django 4.2.6 on 2023-11-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_course_founder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='package_id',
            new_name='package',
        ),
        migrations.AddField(
            model_name='course',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
