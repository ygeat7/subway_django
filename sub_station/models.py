from django.db import models

class BusStation(models.Model):
    stationid = models.IntegerField(blank=True, null=True)
    stationname = models.TextField(blank=True, null=True)
    stationtype = models.TextField(blank=True, null=True)
    stationno = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_station'

    def __str__(self):
        return f'[버스 : {self.stationid}] {self.stationname}'

class SubwayStation(models.Model):
    stationid = models.IntegerField(blank=True, null=True)
    stationname = models.TextField(blank=True, null=True)
    stationno = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    nearbusstcnt = models.FloatField(blank=True, null=True)
    nearbusstno = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subway_station'

    def __str__(self):
        return f'[지하철 : {self.stationid}] {self.stationname}'

class SubTr(models.Model):
    tr_date = models.TextField(blank=True, null=True)
    tr_year = models.IntegerField(blank=True, null=True)
    tr_mon = models.IntegerField(blank=True, null=True)
    st_no = models.TextField(blank=True, null=True)
    st_name = models.TextField(blank=True, null=True)
    number_04_05_getin = models.IntegerField(db_column='04-05_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_04_05_getout = models.IntegerField(db_column='04-05_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_05_06_getin = models.IntegerField(db_column='05-06_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_05_06_getout = models.IntegerField(db_column='05-06_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_06_07_getin = models.IntegerField(db_column='06-07_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_06_07_getout = models.IntegerField(db_column='06-07_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_07_08_getin = models.IntegerField(db_column='07-08_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_07_08_getout = models.IntegerField(db_column='07-08_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_08_09_getin = models.IntegerField(db_column='08-09_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_08_09_getout = models.IntegerField(db_column='08-09_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_09_10_getin = models.IntegerField(db_column='09-10_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_09_10_getout = models.IntegerField(db_column='09-10_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10_11_getin = models.IntegerField(db_column='10-11_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10_11_getout = models.IntegerField(db_column='10-11_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_11_12_getin = models.IntegerField(db_column='11-12_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_11_12_getout = models.IntegerField(db_column='11-12_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_13_getin = models.IntegerField(db_column='12-13_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_13_getout = models.IntegerField(db_column='12-13_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_13_14_getin = models.IntegerField(db_column='13-14_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_13_14_getout = models.IntegerField(db_column='13-14_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_14_15_getin = models.IntegerField(db_column='14-15_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_14_15_getout = models.IntegerField(db_column='14-15_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15_16_getin = models.IntegerField(db_column='15-16_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15_16_getout = models.IntegerField(db_column='15-16_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_16_17_getin = models.IntegerField(db_column='16-17_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_16_17_getout = models.IntegerField(db_column='16-17_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_18_getin = models.IntegerField(db_column='17-18_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_18_getout = models.IntegerField(db_column='17-18_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_18_19_getin = models.IntegerField(db_column='18-19_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_18_19_getout = models.IntegerField(db_column='18-19_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_20_getin = models.IntegerField(db_column='19-20_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_20_getout = models.IntegerField(db_column='19-20_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_20_21_getin = models.IntegerField(db_column='20-21_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_20_21_getout = models.IntegerField(db_column='20-21_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_21_22_getin = models.IntegerField(db_column='21-22_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_21_22_getout = models.IntegerField(db_column='21-22_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_22_23_getin = models.IntegerField(db_column='22-23_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_22_23_getout = models.IntegerField(db_column='22-23_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_23_24_getin = models.IntegerField(db_column='23-24_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_23_24_getout = models.IntegerField(db_column='23-24_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_00_01_getin = models.IntegerField(db_column='00-01_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_00_01_getout = models.IntegerField(db_column='00-01_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_01_02_getin = models.IntegerField(db_column='01-02_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_01_02_getout = models.IntegerField(db_column='01-02_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_02_03_getin = models.IntegerField(db_column='02-03_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_02_03_getout = models.IntegerField(db_column='02-03_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_03_04_getin = models.IntegerField(db_column='03-04_GetIn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_03_04_getout = models.IntegerField(db_column='03-04_GetOut', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    getin_total = models.IntegerField(blank=True, null=True)
    getout_total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_tr'