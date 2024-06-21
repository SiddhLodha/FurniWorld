# Generated by Django 5.0.2 on 2024-03-14 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Delivery Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Failed', 'Failed')], default='Pending', max_length=50),
        ),
    ]
