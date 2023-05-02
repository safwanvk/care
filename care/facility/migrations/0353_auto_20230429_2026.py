# Generated by Django 2.2.11 on 2023-04-29 14:56

import uuid

import django.contrib.postgres.fields.jsonb
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import care.facility.models.mixins.permissions.patient


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facility', '0352_auto_20230428_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftingrequest',
            name='status',
            field=models.IntegerField(choices=[(10, 'PENDING'), (15, 'ON HOLD'), (20, 'APPROVED'), (30, 'REJECTED'),
                                               (40, 'DESTINATION APPROVED'), (50, 'DESTINATION REJECTED'),
                                               (55, 'TRANSPORTATION TO BE ARRANGED'), (60, 'PATIENT TO BE PICKED UP'),
                                               (70, 'TRANSFER IN PROGRESS'), (80, 'COMPLETED'), (90, 'PATIENT EXPIRED'),
                                               (100, 'CANCELLED')], default=10),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('medicine', models.CharField(max_length=100)),
                ('route',
                 models.CharField(blank=True, choices=[('ORAL', 'Oral'), ('IV', 'IV'), ('IM', 'IM'), ('SC', 'S/C')],
                                  max_length=100, null=True)),
                ('dosage', models.CharField(max_length=100)),
                ('is_prn', models.BooleanField(default=False)),
                ('frequency', models.CharField(blank=True, choices=[('STAT', 'Immediately'), ('OD', 'once daily'),
                                                                    ('HS', 'Night only'), ('BD', 'Twice daily'),
                                                                    ('TID', '8th hourly'), ('QID', '6th hourly'),
                                                                    ('Q4H', '4th hourly'), ('QOD', 'Alternate day'),
                                                                    ('QWK', 'Once a week')], max_length=100,
                                               null=True)),
                ('days', models.IntegerField(blank=True, null=True)),
                ('indicator', models.TextField(blank=True, null=True)),
                ('max_dosage', models.CharField(blank=True, max_length=100, null=True)),
                ('min_hours_between_doses', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, default='')),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('discontinued', models.BooleanField(default=False)),
                ('discontinued_reason', models.TextField(blank=True, default='')),
                ('discontinued_date', models.DateTimeField(blank=True, null=True)),
                ('consultation',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facility.PatientConsultation')),
                ('prescribed_by',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, care.facility.models.mixins.permissions.patient.PatientRelatedPermissionMixin),
        ),
        migrations.CreateModel(
            name='MedicineAdministration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('notes', models.TextField(blank=True, default='')),
                ('administered_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('administered_by',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('prescription',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='administrations',
                                   to='facility.Prescription')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='prescription',
            name='daily_round',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT,
                                    to='facility.DailyRound'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='is_migrated',
            field=models.BooleanField(default=False),
        ),
    ]
