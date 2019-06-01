# Generated by Django 2.1.5 on 2019-06-01 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('mobile', models.IntegerField()),
                ('gender', models.CharField(choices=[('m', 'MALE'), ('f', 'FEMALE')], max_length=2)),
            ],
        ),
    ]
