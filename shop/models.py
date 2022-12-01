from django.db import models
from django.utils import timezone
from authentication.models import User
from mptt.models import TreeForeignKey, MPTTModel


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Picture(models.Model):
    picture = models.ImageField()

    def __str__(self):
        return self.picture.url


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField()
    discount = models.IntegerField()
    supplier = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):

    class Rate(models.IntegerChoices):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(choices=Rate.choices)
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='comment_replies')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='comment_replies')

    class Meta:
        ordering = ('creation_date',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.product)


class Cart(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    final_cost = models.FloatField(blank=True, null=True)
