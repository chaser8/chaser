from django.db import models

# Create your models here.
from django.db import models


class AgreeCatalog(models.Model):
    class Meta:
        db_table = "AGREE_CATALOG"

    catalogId = models.IntegerField(db_column="CATALOG_ID", primary_key=True)
    catalogName = models.CharField(db_column="CATALOG_NAME", max_length=100)
    catalogType = models.CharField(db_column="CATALOG_TYPE", max_length=100)
    catalogDesc = models.CharField(db_column="CATALOG_DESC", max_length=100)
    catalogNbr = models.CharField(db_column="CATALOG_NBR", max_length=100)
    catalogUsage = models.CharField(db_column="CATALOG_USAGE", max_length=100)
    applyRegionId = models.CharField(db_column="APPLY_REGION_ID", max_length=100)
    statusCd = models.CharField(db_column="STATUS_CD", max_length=100)
    createStaff = models.IntegerField(db_column="CREATE_STAFF")
    updateStaff = models.IntegerField(db_column="UPDATE_STAFF")
    createDate = models.DateTimeField(db_column="CREATE_DATE")
    updateDate = models.DateTimeField(db_column="UPDATE_DATE")
    statusDate = models.DateTimeField(db_column="STATUS_DATE")
    remark = models.CharField(db_column="REMARK", max_length=100)
