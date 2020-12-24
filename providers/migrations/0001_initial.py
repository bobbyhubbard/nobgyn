# Generated by Django 3.1.2 on 2020-12-24 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_order', models.IntegerField(default=1, help_text='The display order of this provider')),
                ('slug', models.CharField(default='', help_text='URL Path Slug', max_length=25)),
                ('name', models.CharField(help_text='Full name with creds', max_length=50)),
                ('focus', models.CharField(default='Obstetrics & Gynecology', help_text='Ob, Gyn, or both?', max_length=50)),
                ('doctor', models.BooleanField(default=True)),
                ('bio', models.TextField(blank=True, default='', help_text='Bio')),
                ('specialty', models.TextField(help_text='Specialties')),
                ('image_sml', models.FileField(default='', help_text='Small provider image', upload_to='static/images/providers')),
                ('image', models.FileField(default='', help_text='Large provider image', upload_to='static/images/providers')),
            ],
            options={
                'ordering': ['view_order'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeVid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('video_url', models.URLField()),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.provider')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduation_year', models.IntegerField(blank=True, null=True)),
                ('degree', models.TextField(blank=True, default='', help_text='Degree (Optional)')),
                ('ed_type', models.IntegerField(choices=[(1, 'College'), (2, 'Advanced Degree'), (3, 'Medical School'), (4, 'Internship'), (5, 'Residency')], default=1)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.provider')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.school')),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='members',
            field=models.ManyToManyField(through='providers.SchoolRelationship', to='providers.Provider'),
        ),
        migrations.CreateModel(
            name='CertOrgRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certOrg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.certorg')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.provider')),
            ],
        ),
        migrations.AddField(
            model_name='certorg',
            name='members',
            field=models.ManyToManyField(through='providers.CertOrgRelationship', to='providers.Provider'),
        ),
    ]
