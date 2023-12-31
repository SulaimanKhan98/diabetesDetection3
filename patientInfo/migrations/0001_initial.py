# Generated by Django 4.2.6 on 2023-11-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cnic', models.BigIntegerField()),
                ('number', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cnic', models.BigIntegerField()),
                ('number', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('glucose', models.FloatField()),
                ('blood_pressure', models.FloatField()),
                ('skin_thickness', models.FloatField()),
                ('insulin', models.FloatField()),
                ('bmi', models.FloatField()),
                ('diabetes_pedigree_function', models.FloatField()),
                ('prediction_result', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
