from django.db import models

# Create your models here.
class Note(models.Model):
    EVENT_CHOICE = (
        ('idea', 'Edea'),
        ('work', 'Work'),
        ('event', 'Event'),
        ('general', 'General'),
    )
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=EVENT_CHOICE)
    content = models.TextField()
    date = models.DateField(help_text='Date of the note')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

