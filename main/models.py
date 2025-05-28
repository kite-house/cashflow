from django.db import models

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Статус')

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Тип')

    def __str__(self):
        return self.name

class Category(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Категория')

    class Meta:
        unique_together = ('type', 'name')

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Подкатегория')

    class Meta:
        unique_together = ('category', 'name')

    def __str__(self):
        return f"{self.name}"


class Record(models.Model):
    data_created = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=1000, default = "", blank=True)

    def clean(self):
        if self.subcategory.category != self.category:
            raise ValueError('Подкатегория не связана с выбранной категорией')
        
        if self.type != self.category.type:
            raise ValueError('Категория не связана с выбранным типом')
            
