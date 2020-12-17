# Generated by Django 3.1.2 on 2020-10-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_order', models.IntegerField(default=1, help_text='The display order of this service')),
                ('title', models.CharField(default='', help_text='Title', max_length=50)),
                ('desc', models.TextField(default='', help_text='Description (can be html)')),
                ('services', models.TextField(help_text='Services (can be html)')),
                ('sidebar', models.TextField(help_text='Sidebar (can be html)')),
            ],
            options={
                'ordering': ['view_order'],
            },
        ),
    ]
