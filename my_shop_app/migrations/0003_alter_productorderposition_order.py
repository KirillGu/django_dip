# Generated by Django 3.2 on 2021-08-23 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_shop_app', '0002_auto_20210502_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorderposition',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='my_shop_app.order'),
        ),
    ]