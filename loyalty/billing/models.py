from django.db import models

class OnCycle(models.Model):
     active = models.BooleanField(default=True)
     unactive = models.BooleanField(default=False)
     api_key = models.CharField(max_length=10)

     def save(self, *args, **kwargs):
          if self.active = False:
               self.unactive = True
          return super(OnCycle).save(*args, **kwargs)

     def reactive(self):
          if self.unactive = True:
               self.active = True
               self.save()

     def deactivate(self):
          if self.active = False:
               self.unactive = True
               self.save()