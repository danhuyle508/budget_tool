# Generated by Django 2.2 on 2019-04-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0011_auto_20190409_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('Withdrawal', 'withdrawal'), ('Deposit', 'deposit')], default='withdrawal', max_length=16),
        ),
    ]
