# Generated by Django 5.1.3 on 2024-12-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=8)),
            ],
        ),
    ]