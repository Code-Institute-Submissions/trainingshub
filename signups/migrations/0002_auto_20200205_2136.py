# Generated by Django 2.2.9 on 2020-02-05 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('signups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='notes',
            new_name='additional_information',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='country',
        ),
        migrations.AddField(
            model_name='signup',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Courses'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
