# Generated by Django 2.2.2 on 2021-01-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
            ],
        ),
    ]
