from django.db import models

class Todo(models.Model):
    item = models.TextField()
    #user = curren_user
    #작성시간...?

    def __str__(self):
        return self.title



