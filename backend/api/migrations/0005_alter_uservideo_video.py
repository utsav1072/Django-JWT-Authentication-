# Generated by Django 5.0.3 on 2024-03-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_uservideo_video_delete_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservideo',
            name='video',
            field=models.CharField(max_length=100),
        ),
    ]
