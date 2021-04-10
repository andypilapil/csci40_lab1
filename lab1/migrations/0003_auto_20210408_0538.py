# Generated by Django 3.1.7 on 2021-04-07 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0002_auto_20210406_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='foobar', max_length=20)),
                ('key_description', models.CharField(default='foobar', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='key',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='key_description',
        ),
    ]
