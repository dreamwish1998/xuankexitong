# Generated by Django 2.2.7 on 2020-03-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_note_table_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu_table',
            name='note_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='note_status',
            field=models.IntegerField(default=0),
        ),
    ]
