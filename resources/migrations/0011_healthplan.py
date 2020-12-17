# Generated by Django 3.1.2 on 2020-12-15 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0010_auto_20201213_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Health Plan name', max_length=50)),
                ('link', models.URLField(blank=True, default='', help_text='Link (optional)')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
