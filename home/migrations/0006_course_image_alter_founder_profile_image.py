# Generated by Django 4.2.6 on 2023-11-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_package_id_course_package_course_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='static/images/course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='founder',
            name='profile_image',
            field=models.ImageField(upload_to='static/images/founder'),
        ),
    ]
