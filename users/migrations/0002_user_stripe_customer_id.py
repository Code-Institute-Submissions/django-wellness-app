# Generated by Django 3.0.9 on 2020-08-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_customer_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
