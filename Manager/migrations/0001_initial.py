# Generated by Django 2.1.2 on 2018-10-18 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=40)),
                ('destination1', models.CharField(max_length=40)),
                ('destination2', models.CharField(max_length=40)),
                ('destination3', models.CharField(max_length=40)),
                ('destination4', models.CharField(max_length=40)),
                ('destination5', models.CharField(max_length=40)),
                ('destination6', models.CharField(max_length=40)),
                ('destination7', models.CharField(max_length=40)),
                ('destination8', models.CharField(max_length=40)),
                ('destination9', models.CharField(max_length=40)),
                ('destination10', models.CharField(max_length=40)),
                ('no_of_destinations', models.IntegerField()),
            ],
        ),
    ]
