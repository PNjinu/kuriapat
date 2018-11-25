from django.db import models

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    progress = "In Progress"
    done = "Done"
    status_choices = (
        (progress, 'In progress'),
        (done, 'Done')
    )
    status = models.CharField(
        max_length=11,
        choices=status_choices,
        default=done,
    )

    def __str__(self):
        return self.summary
