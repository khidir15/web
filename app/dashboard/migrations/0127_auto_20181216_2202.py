# Generated by Django 2.1.2 on 2018-12-16 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20190118_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='old_profile_rel', to='avatar.Avatar'),
        ),
    ]