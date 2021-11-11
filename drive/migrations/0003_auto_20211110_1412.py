# Generated by Django 3.2.9 on 2021-11-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0002_folder_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='Files')),
            ],
        ),
        migrations.AlterField(
            model_name='folder',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]