# Generated by Django 4.2.6 on 2023-11-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminDetails',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('cnic', models.BigIntegerField()),
                ('number', models.BigIntegerField()),
            ],
        ),
    ]
