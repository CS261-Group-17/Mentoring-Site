# Generated by Django 4.0.2 on 2022-03-12 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('start_datetime', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('cancelled', models.BooleanField(default=False)),
                ('event_type', models.TextField()),
                ('capacity', models.IntegerField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_instructor_meeting', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('start_datetime', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('cancelled', models.BooleanField(default=False)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_instructor_meeting', to=settings.AUTH_USER_MODEL)),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_mentee_meeting', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StrengthWeakness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sw_type', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('sentiment', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WeaknessList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sw_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.strengthweakness')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StrengthList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sw_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.strengthweakness')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField()),
                ('business_area', models.TextField()),
                ('job_title', models.TextField()),
                ('mentor', models.BooleanField(default=False)),
                ('mentee', models.BooleanField(default=True)),
                ('time_available', models.FloatField()),
                ('expert_at', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.strengthweakness')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('code', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pairing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_proposal', models.BooleanField()),
                ('terminated', models.BooleanField()),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentee_pairing', to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_pairing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_datetime', models.DateTimeField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('link', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('complete', models.BooleanField()),
                ('creation_datetime', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('urgency', models.SmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('is_proposed', models.BooleanField(default=False)),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentee_meeting_request', to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_meeting_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('rejection_note', models.TextField(blank=True)),
                ('time1', models.DateTimeField()),
                ('duration1', models.IntegerField()),
                ('time2', models.DateTimeField()),
                ('duration2', models.IntegerField()),
                ('time3', models.DateTimeField()),
                ('duration3', models.IntegerField()),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentee_meeting', to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_meeting', to=settings.AUTH_USER_MODEL)),
                ('request', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.meetingrequest')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('positives', models.TextField(blank=True)),
                ('negatives', models.TextField(blank=True)),
                ('sentiment', models.FloatField()),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_given_feedback', to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.meeting')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupEventFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('positives', models.TextField(blank=True)),
                ('negatives', models.TextField(blank=True)),
                ('sentiment', models.FloatField()),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_given_feedback', to=settings.AUTH_USER_MODEL)),
                ('group_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.groupevent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('positives', models.TextField(blank=True)),
                ('negatives', models.TextField(blank=True)),
                ('sentiment', models.FloatField()),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_given_feedback', to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_received_feedback', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.BooleanField(default=False)),
                ('attendee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.groupevent')),
            ],
        ),
    ]