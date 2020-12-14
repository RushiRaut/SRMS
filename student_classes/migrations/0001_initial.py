# Generated by Django 2.1.3 on 2019-02-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(help_text='Eg- Third, Fouth,Sixth etc', max_length=100)),
                ('class_name_in_numeric', models.IntegerField(help_text='Eg- 1,2,4,5 etc')),
                ('section', models.CharField(help_text='Eg- A,B,C etc', max_length=10)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
