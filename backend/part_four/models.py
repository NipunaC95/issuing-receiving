from django.db import models

# Create your models here.


class IssuedToCCO(models.Model):
    issued_time = models.DateTimeField()
    cco = models.ForeignKey("staffs.Staffs", on_delete=models.SET_NULL)
    i_r_aro = models.ForeignKey("staffs.Staffs", on_delete=models.SET)
    v = models.IntegerField()
    l = models.IntegerField()
    g = models.IntegerField()
    g1 = models.IntegerField()
    z = models.IntegerField()
    election = models.ForeignKey("election.Election", on_delete=models.CASCADE)
    entered_time = models.DateTimeField()
    id = models.AutoField()

    class Meta:
        unique_together = (("id", "entered_time"))


class BallotBoxesIssuedToCCO:
    issued_cco = models.ForeignKey("IssuedToCCO", on_delete=models.CASCADE)
    serial_number = models.CharField()
