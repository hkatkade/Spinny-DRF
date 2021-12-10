# Generated by Django 3.1.6 on 2021-12-07 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0010_auto_20211207_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='updator',
        ),
        migrations.AddField(
            model_name='box',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]