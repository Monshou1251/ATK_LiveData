# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CdcConn(models.Model):
    conn_type = models.CharField(max_length=128, blank=True, null=True)
    conn_name = models.CharField(primary_key=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'cdc_conn'


class CdcFields(models.Model):
    table_id = models.CharField(primary_key=True, max_length=128)
    source_field_name = models.CharField(max_length=128)
    target_field_name = models.CharField(max_length=128, blank=True, null=True)
    field_index = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True)
    field_type = models.CharField(max_length=40, blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)
    pk_field = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True, db_column='pk')
    required = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdc_fields'
        unique_together = (('table_id', 'source_field_name'),)


class CdcStatus(models.Model):
    table_id = models.CharField(primary_key=True, max_length=128)
    last_read_seq = models.CharField(max_length=35, blank=True, null=True)
    init_read_seq = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdc_status'


class CdcTables(models.Model):
    table_id = models.CharField(primary_key=True, max_length=128)
    source_db = models.CharField(max_length=128, blank=True, null=True)
    source_schema = models.CharField(max_length=128, blank=True, null=True)
    source_table = models.CharField(max_length=128, blank=True, null=True)
    target_schema = models.CharField(max_length=128, blank=True, null=True)
    target_table = models.CharField(max_length=128, blank=True, null=True)
    uppercase_fields = models.DecimalField(
        max_digits=18, decimal_places=0, blank=True, null=True)
    filter = models.CharField(max_length=128, blank=True, null=True)
    force_init = models.CharField(max_length=128, blank=True, null=True)
    cntrl_fld = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdc_tables'


# class TestTable(models.Model):

#     testname = models.CharField(max_length=255)
#     testsurname = models.CharField(max_length=255)
#     testdate = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['id']
