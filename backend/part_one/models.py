from django.db import models

# Create your models here.


class ReportedToWorkElectionDay(models.Model):
    time = models.TimeField()
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
    staff = models.ForeignKey("staffs.Staffs", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["election, staff"],name="election_staff")
        ]


class ReportedToWorkBeforeElection(models.Model):
    time = models.TimeField()
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
    staff = models.ForeignKey("staffs.Staffs", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["election, staff"], name="election_staff")
        ]
