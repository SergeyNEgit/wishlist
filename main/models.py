from django.db import models
from django.db.models.base import Model

class Product(Model):
    """
    Таблица "Товар"
    id
    ...
    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title
    
