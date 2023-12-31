# Generated by Django 4.2.6 on 2023-11-05 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_course_image_alter_founder_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.package'),
        ),
    ]
