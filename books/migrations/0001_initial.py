# Generated by Django 2.0.1 on 2018-01-11 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=70)),
                ('review', models.TextField(blank=True, null=True)),
                ('date_reviewed', models.DateTimeField(blank=True, null=True)),
                ('is_favourite', models.BooleanField(default=False)),
            ],
        ),
    ]
