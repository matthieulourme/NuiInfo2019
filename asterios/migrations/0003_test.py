# Generated by Django 2.1 on 2019-12-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asterios', '0002_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=200)),
            ],
        ),
    ]