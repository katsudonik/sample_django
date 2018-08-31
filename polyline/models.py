from django.db import models
from django.utils import timezone

class SoilDisposalTask(models.Model):
    at_time_field_latitude  = models.DecimalField(max_digits=10, decimal_places=8)
    at_time_field_longitude  = models.DecimalField(max_digits=11, decimal_places=8)
    at_time_soil_disposal_site_latitude  = models.DecimalField(max_digits=10, decimal_places=8)
    at_time_soil_disposal_site_longitude  = models.DecimalField(max_digits=11, decimal_places=8)
    image_path  = models.TextField()
    mileage = models.DecimalField(max_digits=8, decimal_places=0)
    co2_emissions  = models.DecimalField(max_digits=13, decimal_places=3)
    arrived_to_site_flg  = models.BooleanField()
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'soil_disposal_tasks'

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.image_path

