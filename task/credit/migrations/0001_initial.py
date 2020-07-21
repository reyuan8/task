# Generated by Django 3.0.8 on 2020-07-21 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'Заблокированный',
                'verbose_name_plural': 'Заблокированные',
            },
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', models.CharField(max_length=12)),
                ('birth_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Заёмщик',
                'verbose_name_plural': 'Заёмщики',
            },
        ),
        migrations.CreateModel(
            name='CreditProgramm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_amount', models.PositiveIntegerField(verbose_name='Минимальная сумма')),
                ('max_amount', models.PositiveIntegerField(verbose_name='Максимальная сумма')),
                ('min_age', models.PositiveIntegerField(verbose_name='Минимальный возраст')),
                ('max_age', models.PositiveIntegerField(verbose_name='Максимальный возраст')),
            ],
            options={
                'verbose_name': 'Кредитная программа',
                'verbose_name_plural': 'Кредитные программы',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Сумма')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Accepted'), (2, 'Declined')])),
                ('rejection_reason', models.TextField(blank=True, max_length=100, null=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='credit.Borrower')),
                ('programm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='credit.CreditProgramm')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]