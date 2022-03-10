# Generated by Django 4.0.2 on 2022-03-09 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_strengthlist_weaknesslist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingweaknesses',
            name='event',
        ),
        migrations.RemoveField(
            model_name='meetingweaknesses',
            name='weakness_type',
        ),
        migrations.RemoveField(
            model_name='meetingproposal',
            name='description',
        ),
        migrations.RemoveField(
            model_name='meetingrequest',
            name='proposal',
        ),
        migrations.AddField(
            model_name='meetingproposal',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='meetingproposal',
            name='request',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.meetingrequest'),
        ),
        migrations.AddField(
            model_name='meetingrequest',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='meetingrequest',
            name='is_proposed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='meetingproposal',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='GroupEventWeaknesses',
        ),
        migrations.DeleteModel(
            name='MeetingWeaknesses',
        ),
    ]
