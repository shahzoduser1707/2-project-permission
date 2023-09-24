# Generated by Django 4.2.5 on 2023-09-23 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonemodel',
            name='creator_name_en',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='creator_name_ru',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='creator_name_uz',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='name_en',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='name_ru',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='name_uz',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='power_en',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='power_ru',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='power_uz',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]