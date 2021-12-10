# Generated by Django 3.1.6 on 2021-12-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(blank=True, max_length=100, null=True)),
                ('updator', models.CharField(blank=True, max_length=100, null=True)),
                ('length', models.IntegerField(blank=True, default=0, null=True)),
                ('width', models.IntegerField(blank=True, default=0, null=True)),
                ('height', models.IntegerField(blank=True, default=0, null=True)),
                ('volume', models.IntegerField(blank=True, default=0, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]