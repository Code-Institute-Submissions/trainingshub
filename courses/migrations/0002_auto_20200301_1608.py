# Generated by Django 2.2.10 on 2020-03-01 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_type',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Course_type'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Location'),
        ),
    ]
