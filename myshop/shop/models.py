from django.db import models
from django.urls import reverse

def convert(price) -> str:
    price = str(price)
    res = "" 
    for i in range(len(price), 0, -1):
        if i % 3 == 0:
            res += " " + price[-i]
        else:
            res += price[-i]
    return res.lstrip()

def back(price) -> int:
    if price == "":
        return 0
    else:
        return int(price.replace(" ", ""))


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
    def get_price(self):
        if self.price == "":
            return 0
        else:
            return convert(self.price)
    
    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])
