from django.db import models

# Create your models here.


class Customers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    person = models.TextField(db_column='PERSON', blank=True, null=True)  # Field name made lowercase.
    website = models.TextField(db_column='WEBSITE', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.person


    class Meta:
        managed = False
        db_table = 'customers'