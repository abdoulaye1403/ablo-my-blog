# Generated by Django 2.2.2 on 2020-12-31 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('creer_le', models.DateTimeField(auto_now_add=True)),
                ('modifier_le', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
