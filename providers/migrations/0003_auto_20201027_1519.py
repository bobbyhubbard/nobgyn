# Generated by Django 3.1.2 on 2020-10-27 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_auto_20201027_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ed_type', models.IntegerField(choices=[(1, 'College'), (2, 'Advanced Degree'), (3, 'Medical School'), (4, 'Internship'), (5, 'Residency')], default=1)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.provider')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.school')),
            ],
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.AddField(
            model_name='school',
            name='members',
            field=models.ManyToManyField(through='providers.SchoolRelationship', to='providers.Provider'),
        ),
    ]