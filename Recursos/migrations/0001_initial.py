# Generated by Django 4.0.3 on 2022-05-13 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biblias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('version_año', models.DateField(auto_now_add=True)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Biblia',
                'verbose_name_plural': 'Biblias',
            },
        ),
    ]
