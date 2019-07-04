# Generated by Django 2.0.2 on 2019-07-04 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20190704_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='feature_voted',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.FeaturePost'),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order'),
        ),
    ]