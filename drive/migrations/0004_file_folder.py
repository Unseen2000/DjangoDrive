# Generated by Django 3.2.9 on 2021-11-10 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0003_auto_20211110_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='drive.folder'),
            preserve_default=False,
        ),
    ]