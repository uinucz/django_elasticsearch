# Generated by Django 3.1.7 on 2023-03-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '3'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineSearchWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
