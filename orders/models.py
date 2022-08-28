from django.db import models


class MenuItemCustomizationOption(models.Model):
    name = models.CharField(max_length=255, default="Customization Option")


class MenuItemCustomization(models.Model):
    name = models.CharField(max_length=255, default="Item Customization")
    options = models.CharField(choices=MenuItemCustomizationOption)
    allow_multiple = models.BooleanField(default=False)


class MenuItem(models.Model):
    pass


class Order(models.Model):
    pass


class MenuSection(models.Model):
    pass

