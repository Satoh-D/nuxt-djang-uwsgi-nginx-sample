# Generated by Django 2.2.16 on 2020-10-07 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.TextField()),
                ('person_age', models.IntegerField()),
            ],
        ),
    ]
