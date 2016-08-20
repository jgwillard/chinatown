# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('synced', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeping.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeping.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Reimbursement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('synced', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeping.Book')),
                ('paid_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reimbursement_paid_by', to='bookkeeping.Participant')),
                ('paid_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reimbursement_paid_to', to='bookkeeping.Participant')),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='paid_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeping.Participant'),
        ),
    ]