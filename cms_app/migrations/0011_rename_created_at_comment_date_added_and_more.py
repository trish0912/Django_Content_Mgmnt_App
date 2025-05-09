# Generated by Django 4.2.18 on 2025-02-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0010_rename_date_added_comment_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='message',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='nice', max_length=50),
            preserve_default=False,
        ),
    ]
