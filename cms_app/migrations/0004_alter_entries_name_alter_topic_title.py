# Generated by Django 4.2.18 on 2025-02-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0003_alter_entries_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
