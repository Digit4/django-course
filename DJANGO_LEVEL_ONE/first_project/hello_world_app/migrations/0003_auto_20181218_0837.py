# Generated by Django 2.1.2 on 2018-12-18 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world_app', '0002_auto_20181218_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrecord',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hello_world_app.WebPage'),
        ),
    ]
