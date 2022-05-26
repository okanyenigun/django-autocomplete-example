# Generated by Django 4.0.4 on 2022-05-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('person', models.TextField(blank=True, db_column='PERSON', null=True)),
                ('website', models.TextField(blank=True, db_column='WEBSITE', null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
    ]