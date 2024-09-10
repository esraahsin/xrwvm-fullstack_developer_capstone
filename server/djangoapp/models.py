from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    # - Name: This field stores the name of the car make (e.g., Toyota, Honda)
    name = models.CharField(max_length=100)

    # - Description: This field stores a description of the car make
    description = models.TextField()

    # - Any other fields you would like to include in the car make model
    # (e.g., origin_country or founded_year could be added as extra fields if needed)
    # Extra fields are optional and can be added here based on your application's requirements

    # - __str__ method to print a car make object
    # This method returns the name of the car make when printed or referenced as a string
    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    # - Many-To-One relationship to Car Make model:
    # One Car Make can have many Car Models, but each Car Model is linked to one Car Make
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    # - Name: This field stores the name of the car model (e.g., Camry, Civic)
    name = models.CharField(max_length=100)

    # - Type (CharField with a choices argument):
    # Provide limited choices such as Sedan, SUV, WAGON, etc.
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more types if needed
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    # - Year (IntegerField) with min value 2015 and max value 2023:
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),  # Max year is 2023
            MinValueValidator(2015)   # Min year is 2015
        ]
    )

    # - Any other fields you would like to include in the car model:
    # Optional additional fields like color or dealer ID
    color = models.CharField(max_length=50, blank=True, null=True)
    dealer_id = models.IntegerField()

    # - __str__ method to print a car make object:
    # This method returns the car make and car model when printed or referenced as a string
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
