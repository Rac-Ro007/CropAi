# Generated by Django 2.1.5 on 2019-03-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fertilizer_shop', '0005_auto_20190302_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizer',
            name='buyer',
            field=models.CharField(max_length=30),
        ),
    ]