# Generated by Django 2.0 on 2020-03-05 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_auto_20200303_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_login',
            name='gh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='school.Teacher'),
        ),
    ]
