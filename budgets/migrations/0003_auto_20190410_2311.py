# Generated by Django 2.2 on 2019-04-10 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0002_auto_20190410_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('withdrawal', 'Withdrawal'), ('deposit', 'Deposit')], default='Withdrawal', max_length=16),
        ),
    ]