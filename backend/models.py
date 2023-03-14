# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Afrinic20220424(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'afrinic_2022_04_24'


class Afrinic20220425(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'afrinic_2022_04_25'


class Afrinic20220505(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_05'


class Afrinic20220507(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_07'


class Afrinic20220509(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_09'


class Afrinic20220510(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_10'


class Afrinic20220522(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_22'


class Afrinic20220523(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_23'


class Afrinic20220524(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_24'


class Afrinic20220525(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_25'


class Afrinic20220526(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_26'


class Afrinic20220529(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_29'


class Afrinic20220530(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_30'


class Afrinic20220531(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'afrinic_2022_05_31'


class Afrinic20220601(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'afrinic_2022_06_01'


class Apnic20220510(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apnic_2022_05_10'


class Apnic20220522(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'apnic_2022_05_22'


class Apnic20220523(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'apnic_2022_05_23'


class Apnic20220524(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'apnic_2022_05_24'


class Apnic20220525(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'apnic_2022_05_25'


class Apnic20220526(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'apnic_2022_05_26'


class Apnic20220529(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'apnic_2022_05_29'


class Apnic20220530(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'apnic_2022_05_30'


class Apnic20220531(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'apnic_2022_05_31'


class Apnic20220601(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'apnic_2022_06_01'


class Arin20220510(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'arin_2022_05_10'


class Arin20220522(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'arin_2022_05_22'


class Arin20220523(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'arin_2022_05_23'


class Arin20220524(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'arin_2022_05_24'


class Arin20220525(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'arin_2022_05_25'


class Arin20220526(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'arin_2022_05_26'


class Arin20220529(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'arin_2022_05_29'


class Arin20220530(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'arin_2022_05_30'


class Arin20220531(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'arin_2022_05_31'


class Arin20220601(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'arin_2022_06_01'


class AsnIp20220504(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('Roa20220504', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asn_ip_2022_05_04'


class AsnIp20220505(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('Roa20220505', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asn_ip_2022_05_05'


class AsnIp20220507(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('Roa20220507', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asn_ip_2022_05_07'


class AsnIp20220509(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('Roa20220509', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asn_ip_2022_05_09'


class AsnIp20220510(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('Roa20220510', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asn_ip_2022_05_10'


class AsnIp20220520(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('Roa20220520', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asn_ip_2022_05_20'


class AsnIp20220521(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('Roa20220521', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asn_ip_2022_05_21'


class AsnIpRipe20220522(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('RoaRipe20220522', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.
    # id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asn_ip_ripe_2022_05_22'


class AsnIpRipe20220523(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('RoaRipe20220523', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.
    # id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asn_ip_ripe_2022_05_23'


class AsnIpRipe20220524(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('RoaRipe20220524', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.
    # id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asn_ip_ripe_2022_05_24'


class AsnIpRipe20220525(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('RoaRipe20220525', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.
    # id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asn_ip_ripe_2022_05_25'


class AsnIpRipe20220526(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('RoaRipe20220526', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.
    # id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asn_ip_ripe_2022_05_26'


class AsnIpRipe20220529(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('RoaRipe20220529', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.
    # id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asn_ip_ripe_2022_05_29'


class AsnIpRipe20220530(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('RoaRipe20220530', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.
    # id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asn_ip_ripe_2022_05_30'


class AsnIpRipe20220531(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('RoaRipe20220531', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.
    # id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asn_ip_ripe_2022_05_31'


class AsnIpRipe20220601(models.Model):
    asn = models.CharField(db_column='ASN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip_block = models.CharField(db_column='IP_block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=5, blank=True, null=True)
    max_length = models.CharField(max_length=5, blank=True, null=True)
    roa_uri = models.ForeignKey('RoaRipe20220601', models.DO_NOTHING, db_column='ROA_URI', blank=True, null=True)  # Field name made lowercase.
    # id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asn_ip_ripe_2022_06_01'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Certificate20220504(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certificate_2022_05_04'


class Certificate20220505(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certificate_2022_05_05'


class Certificate20220507(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certificate_2022_05_07'


class Certificate20220509(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certificate_2022_05_09'


class Certificate20220510(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certificate_2022_05_10'


class Certificate20220520(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certificate_2022_05_20'


class Certificate20220521(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certificate_2022_05_21'


class CertificateRipe20220522(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_ripe_2022_05_22'


class CertificateRipe20220523(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_ripe_2022_05_23'


class CertificateRipe20220524(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_ripe_2022_05_24'


class CertificateRipe20220525(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_ripe_2022_05_25'


class CertificateRipe20220526(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_ripe_2022_05_26'


class CertificateRipe20220529(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_ripe_2022_05_29'


class CertificateRipe20220530(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_ripe_2022_05_30'


class CertificateRipe20220531(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_ripe_2022_05_31'


class CertificateRipe20220601(models.Model):
    cert_name = models.CharField(db_column='Cert_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cert_uri = models.CharField(db_column='Cert_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    auth_uri = models.CharField(db_column='Auth_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sub_uri = models.CharField(db_column='Sub_URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_ripe_2022_06_01'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Lacnic20220510(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lacnic_2022_05_10'


class Lacnic20220522(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'lacnic_2022_05_22'


class Lacnic20220523(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'lacnic_2022_05_23'


class Lacnic20220524(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'lacnic_2022_05_24'


class Lacnic20220525(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'lacnic_2022_05_25'


class Lacnic20220526(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'lacnic_2022_05_26'


class Lacnic20220529(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'lacnic_2022_05_29'


class Lacnic20220530(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'lacnic_2022_05_30'


class Lacnic20220531(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'lacnic_2022_05_31'


class Lacnic20220601(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'lacnic_2022_06_01'


class Ripencc20220510(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ripencc_2022_05_10'


class Ripencc20220522(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'ripencc_2022_05_22'


class Ripencc20220523(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'ripencc_2022_05_23'


class Ripencc20220524(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'ripencc_2022_05_24'


class Ripencc20220525(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'ripencc_2022_05_25'


class Ripencc20220526(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'ripencc_2022_05_26'


class Ripencc20220529(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'ripencc_2022_05_29'


class Ripencc20220530(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'ripencc_2022_05_30'


class Ripencc20220531(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'ripencc_2022_05_31'


class Ripencc20220601(models.Model):
    uri = models.CharField(db_column='URI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asn = models.CharField(db_column='ASN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip_pre = models.CharField(db_column='IP_pre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_len = models.CharField(db_column='Max_len', max_length=10, blank=True, null=True)  # Field name made lowercase.
    not_before = models.CharField(db_column='Not_Before', max_length=50, blank=True, null=True)  # Field name made lowercase.
    not_after = models.CharField(db_column='Not_After', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'ripencc_2022_06_01'


class Roa20220504(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(Certificate20220504, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roa_2022_05_04'


class Roa20220505(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(Certificate20220505, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roa_2022_05_05'


class Roa20220507(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(Certificate20220507, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roa_2022_05_07'


class Roa20220509(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(Certificate20220509, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roa_2022_05_09'


class Roa20220510(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(Certificate20220510, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roa_2022_05_10'


class Roa20220520(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(Certificate20220520, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roa_2022_05_20'


class Roa20220521(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(Certificate20220521, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roa_2022_05_21'


class RoaRipe20220522(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(CertificateRipe20220522, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roa_ripe_2022_05_22'


class RoaRipe20220523(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(CertificateRipe20220523, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roa_ripe_2022_05_23'


class RoaRipe20220524(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(CertificateRipe20220524, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roa_ripe_2022_05_24'


class RoaRipe20220525(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(CertificateRipe20220525, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roa_ripe_2022_05_25'


class RoaRipe20220526(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(CertificateRipe20220526, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roa_ripe_2022_05_26'


class RoaRipe20220529(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(CertificateRipe20220529, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roa_ripe_2022_05_29'


class RoaRipe20220530(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(CertificateRipe20220530, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roa_ripe_2022_05_30'


class RoaRipe20220531(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(CertificateRipe20220531, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roa_ripe_2022_05_31'


class RoaRipe20220601(models.Model):
    roa_name = models.CharField(db_column='ROA_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roa_uri = models.CharField(db_column='ROA_URI', primary_key=True, max_length=200)  # Field name made lowercase.
    cert_uri = models.ForeignKey(CertificateRipe20220601, models.DO_NOTHING, db_column='Cert_URI', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roa_ripe_2022_06_01'


class Rov(models.Model):
    prefix = models.CharField(max_length=200, blank=True, null=True)
    origin = models.CharField(max_length=200, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=50, blank=True, null=True)
    reason = models.CharField(max_length=200, blank=True, null=True)
    first_time = models.IntegerField(blank=True, null=True)
    last_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rov'
