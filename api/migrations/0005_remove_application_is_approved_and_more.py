# Generated by Django 4.1.3 on 2022-11-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_slot_applicant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='application',
            name='is_slot_allotted',
            field=models.BooleanField(default=False),
        ),
    ]