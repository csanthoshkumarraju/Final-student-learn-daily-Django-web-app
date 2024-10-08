# Generated by Django 5.1.1 on 2024-09-24 16:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPuzzleGuessGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_attempts', models.IntegerField(default=0)),
                ('total_correct_answers', models.IntegerField(default=0)),
                ('success_percentage', models.FloatField(default=0.0)),
                ('last_played', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
