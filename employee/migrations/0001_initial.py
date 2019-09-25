# Generated by Django 2.2.5 on 2019-09-23 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('manager', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Employe',
                'verbose_name_plural': 'Employes',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default='employee', max_length=50, verbose_name='Position')),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employe', verbose_name='emp_position')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('requested', 'Requested'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='', max_length=50)),
                ('LEave_type', models.CharField(choices=[('leave', 'Leave'), ('execuse', 'Execuse')], default='', max_length=50)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employe', verbose_name='emp_leaves')),
            ],
            options={
                'verbose_name': 'Leaves',
                'verbose_name_plural': 'Leaves',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employe', verbose_name='Emp_department')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
    ]