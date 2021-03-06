# Generated by Django 2.2 on 2019-04-10 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0007_auto_20190410_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date_completed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
    ]
