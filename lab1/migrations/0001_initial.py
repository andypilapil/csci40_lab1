# Generated by Django 3.1.7 on 2021-04-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('profile_nickname', models.CharField(max_length=10)),
                ('profile_bio', models.CharField(max_length=50)),
            ],
        ),
    ]
