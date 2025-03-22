from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

# todo  model manager to build method to filter products based on available field
class MyManager(models.Manager):
    def get_available_product(self):
        return self.filter(available=True)

class Product(models.Model):
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"))
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    # todo add available field to the model
    available = models.BooleanField(_("available"), default=False)

    # todo must add 
    objects = MyManager()
    


    def __str__(self):
        return self.name