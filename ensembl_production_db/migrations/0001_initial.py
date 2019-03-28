# Generated by Django 2.1.7 on 2019-03-27 23:56

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion
import django_mysql.models
import ensembl_production.models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisDescription',
            fields=[
                ('created_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL, blank=True, db_column='created_by', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='modified_by', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('is_current', models.BooleanField(default=True)),
                ('analysis_description_id', models.AutoField(primary_key=True, serialize=False)),
                ('logic_name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('display_label', models.CharField(max_length=256)),
                ('db_version', models.BooleanField(default=True, verbose_name='Use DB version')),
                ('displayable', models.BooleanField(default=True, verbose_name='Is displayed')),
            ],
            options={
                'db_table': 'analysis_description',
            },
        ),
        migrations.CreateModel(
            name='MasterAttrib',
            fields=[
                ('created_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='created_by', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='modified_by', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('is_current', models.BooleanField(default=True)),
                ('attrib_id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Attrib',
                'db_table': 'master_attrib',
            },
        ),
        migrations.CreateModel(
            name='MasterAttribType',
            fields=[
                ('created_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='created_by', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='modified_by', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('is_current', models.BooleanField(default=True)),
                ('attrib_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'AttribType',
                'db_table': 'master_attrib_type',
            },
        ),
        migrations.CreateModel(
            name='MasterBiotype',
            fields=[
                ('created_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='created_by', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='modified_by', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('is_current', models.BooleanField(default=True)),
                ('biotype_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('is_dumped', models.BooleanField(default=True)),
                ('object_type', django_mysql.models.EnumField(choices=[('gene', 'gene'), ('transcript', 'transcript')], default='gene')),
                ('db_type', multiselectfield.db.fields.MultiSelectField(choices=[('cdna', 'cdna'), ('core', 'core'), ('coreexpressionatlas', 'coreexpressionatlas'), ('coreexpressionest', 'coreexpressionest'), ('coreexpressiongnf', 'coreexpressiongnf'), ('funcgen', 'funcgen'), ('otherfeatures', 'otherfeatures'), ('rnaseq', 'rnaseq'), ('variation', 'variation'), ('vega', 'vega'), ('presite', 'presite'), ('sangervega', 'sangervega')], default='core', max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('biotype_group', django_mysql.models.EnumField(choices=[('coding', 'coding'), ('pseudogene', 'pseudogene'), ('snoncoding', 'snoncoding'), ('lnoncoding', 'lnoncoding'), ('mnoncoding', 'mnoncoding'), ('LRG', 'LRG'), ('undefined', 'undefined'), ('no_group', 'no_group')], default='no_group')),
                ('so_acc', models.CharField(blank=True, max_length=64, null=True)),
                ('so_term', models.CharField(blank=True, max_length=1023, null=True)),
                ('attrib_type', models.ForeignKey(blank=True, db_column='attrib_type_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ensembl_production_db.MasterAttribType')),
            ],
            options={
                'verbose_name': 'Biotype',
                'db_table': 'master_biotype',
            },
        ),
        migrations.CreateModel(
            name='MasterExternalDb',
            fields=[
                ('created_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='created_by', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='modified_by', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('is_current', models.BooleanField(default=True)),
                ('external_db_id', models.AutoField(primary_key=True, serialize=False)),
                ('db_name', models.CharField(max_length=100)),
                ('db_release', models.CharField(blank=True, max_length=255, null=True)),
                ('status', django_mysql.models.EnumField(choices=[('KNOWNXREF', 'KNOWNXREF'), ('KNOWN', 'KNOWN'), ('XREF', 'XREF'), ('PRED', 'PRED'), ('ORTH', 'ORTH'), ('PSEUDO', 'PSEUDO')])),
                ('priority', models.IntegerField()),
                ('db_display_name', models.CharField(max_length=255)),
                ('type', django_mysql.models.EnumField(choices=[('ARRAY', 'ARRAY'), ('ALT_TRANS', 'ALT_TRANS'), ('ALT_GENE', 'ALT_GENE'), ('MISC', 'MISC'), ('LIT', 'LIT'), ('PRIMARY_DB_SYNONYM', 'PRIMARY_DB_SYNONYM'), ('ENSEMBL', 'ENSEMBL')])),
                ('secondary_db_name', models.CharField(blank=True, max_length=255, null=True)),
                ('secondary_db_table', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'ExternalDB',
                'db_table': 'master_external_db',
            },
        ),
        migrations.CreateModel(
            name='MasterMiscSet',
            fields=[
                ('created_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='created_by', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='modified_by', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('is_current', models.BooleanField(default=True)),
                ('misc_set_id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=25, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('max_length', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'master_misc_set',
            },
        ),
        migrations.CreateModel(
            name='MasterUnmappedReason',
            fields=[
                ('created_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='created_by', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='modified_by', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('is_current', models.BooleanField(default=True)),
                ('unmapped_reason_id', models.AutoField(primary_key=True, serialize=False)),
                ('summary_description', models.CharField(blank=True, max_length=255, null=True)),
                ('full_description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'master_unmapped_reason',
            },
        ),
        migrations.CreateModel(
            name='MetaKey',
            fields=[
                ('created_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='created_by', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='modified_by', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('is_current', models.BooleanField(default=True)),
                ('meta_key_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('is_optional', models.BooleanField(default=False)),
                ('db_type', multiselectfield.db.fields.MultiSelectField(choices=[('cdna', 'cdna'), ('compara', 'compara'), ('core', 'core'), ('funcgen', 'funcgen'), ('otherfeatures', 'otherfeatures'), ('rnaseq', 'rnaseq'), ('variation', 'variation'), ('vega', 'vega'), ('presite', 'presite'), ('sangervega', 'sangervega')], max_length=80)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'meta_key',
            },
        ),
        migrations.CreateModel(
            name='WebData',
            fields=[
                ('created_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='created_by', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='modified_by', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('web_data_id', models.AutoField(primary_key=True, serialize=False)),
                ('web_data', ensembl_production.models.PerlField(db_column='data', null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'WebData',
                'db_table': 'web_data',
            },
        ),
        migrations.CreateModel(
            name='MasterAttribSet',
            fields=[
                ('created_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='created_by', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_by', ensembl_production.models.SpanningForeignKey(settings.AUTH_USER_MODEL,blank=True, db_column='modified_by', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('is_current', models.BooleanField(default=True)),
                ('attrib_set_id', models.IntegerField()),
                ('attrib', models.OneToOneField(db_column='attrib_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='related_attrib_set', serialize=False, to='ensembl_production_db.MasterAttrib')),
            ],
            options={
                'verbose_name': 'AttribSet',
                'db_table': 'master_attrib_set',
            },
        ),
        migrations.AlterUniqueTogether(
            name='masterexternaldb',
            unique_together={('db_name', 'db_release', 'is_current')},
        ),
        migrations.AddField(
            model_name='masterattrib',
            name='attrib_type',
            field=models.ForeignKey(db_column='attrib_type_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ensembl_production_db.MasterAttribType'),
        ),
        migrations.AddField(
            model_name='analysisdescription',
            name='web_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='analysis', to='ensembl_production_db.WebData'),
        ),
        migrations.AlterUniqueTogether(
            name='masterbiotype',
            unique_together={('name', 'object_type')},
        ),
    ]
