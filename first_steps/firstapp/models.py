from django.db import models

# Create your models here.
class Tour(models.Model):
    '''
        - origin country
        - destination
        - number of nights
        - price for the tour
    '''
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    # String representation of the tours
    def __str__(self):
        return (f"ID:{self.id}: From {self.origin_country}"
                f" To {self.destination_country} for {self.number_of_nights} nights "
                f"at a price of {self.price}$")