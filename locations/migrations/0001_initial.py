# Generated by Django 3.1.2 on 2020-11-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(default='', help_text='URL Path Slug', max_length=25)),
                ('view_order', models.IntegerField(default=1, help_text='The display order of this location')),
                ('name', models.TextField(default='', help_text='Name')),
                ('parent_facility', models.TextField(default='', help_text='The name of the parent facility (eg "Liberty Hospital")')),
                ('address', models.TextField(default='', help_text='Address')),
                ('image_sml', models.FileField(default='', help_text='Small location image', upload_to='static/images/locations')),
                ('image', models.FileField(default='', help_text='Large location image', upload_to='static/images/locations')),
                ('appointment_text', models.TextField(default='8am- 5pm  Monday - Friday', help_text='Display text for appointments')),
                ('phone', models.CharField(default='(816) 781-7820', help_text='Phone display text', max_length=14)),
                ('desc', models.TextField(default='', help_text='Description (can be html)')),
                ('highlighted_content', models.TextField(help_text='Special content to highlight (can be html)')),
            ],
            options={
                'ordering': ['view_order'],
            },
        ),
    ]
