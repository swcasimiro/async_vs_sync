from django.db import models


class Category(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=40
    )

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(
        'Название продукта',
        max_length=40
    )
    description = models.TextField(
        'Описание продукта',
        max_length=4000
    )
    cat = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.name

