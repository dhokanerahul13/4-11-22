# Generated by Django 4.1.1 on 2022-11-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile_no', models.IntegerField()),
                ('feedback', models.TextField()),
            ],
        ),
    ]
