# Generated by Django 4.1.1 on 2022-11-02 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='employee',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='scheduler.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='availability',
            name='numberOfHours',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='skills',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='skill_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]