from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, EmailValidator, FileExtensionValidator
from django.core.exceptions import ValidationError

class Person(models.Model):
     name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        validators=[
            MaxLengthValidator(30, message="Entrer moins de 30 caractères"),
            MinLengthValidator(2, message="Entrer plus de deux caractères")
        ]
    )

class Contact(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        validators=[
            MaxLengthValidator(30, message="Entrer moins de 30 caractères"),
            MinLengthValidator(2, message="Entrer plus de deux caractères")
        ]
    )
    phone_number = models.CharField(
        max_length=30,  # Adjusted to a reasonable length for phone numbers
        blank=False,
        null=False
    )
    email = models.EmailField(
        blank=False,
        null=False,
        validators=[EmailValidator(message="Entrer un email valide")]
    )

    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)


    face_id = models.ImageField(upload_to="images/profileimage/", null=True, blank= True)
    # face_id = models.ImageField(upload_to="images/profileimage/", null=True, blank= True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    def __str__(self):
        return self.name
    
    def clean_phone_number(self):
        phone = self.phone_number
        if len(phone) < 2:
            raise ValidationError(message="phone number should be greate that 2")