# Generated by Django 2.0.2 on 2019-07-04 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0004_auto_20190704_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bugs', to='bugs.BugPost'),
        ),
    ]