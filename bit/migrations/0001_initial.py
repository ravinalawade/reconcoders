# Generated by Django 2.1.7 on 2019-03-30 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms_disease', models.CharField(max_length=200)),
                ('disease_possible', models.CharField(max_length=200)),
                ('medicine', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=200)),
                ('doctor_address', models.CharField(max_length=200)),
                ('doctor_bdate', models.DateField()),
                ('doctor_number', models.CharField(max_length=10)),
                ('doctor_gender', models.CharField(max_length=1)),
                ('doctor_username', models.CharField(max_length=200)),
                ('doctor_pass', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=200)),
                ('patient_address', models.CharField(max_length=200)),
                ('bdate', models.DateField()),
                ('patient_number', models.IntegerField(max_length=10)),
                ('patient_gender', models.CharField(max_length=1)),
                ('patient_username', models.CharField(max_length=200)),
                ('patient_pass', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='disease',
            name='patient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bit.Patient'),
        ),
    ]
