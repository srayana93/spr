from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock_quantity = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    vendor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='vendor_products')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_discounted_price(self):
        if self.discount_price:
            return self.discount_price
        return self.price

    @classmethod
    def bulk_create_from_csv(cls, csv_file, vendor):
        """
        Bulk creates products from a CSV file.
        The CSV should have the following columns: 
        name, description, sku, price, discount_price, stock_quantity, category
        """
        products = []
        reader = csv.DictReader(csv_file)

        for row in reader:
            category = Category.objects.get(name=row['category'])
            product = cls(
                name=row['name'],
                description=row['description'],
                slug=row['sku'],  # Assuming SKU as a unique identifier and slug
                sku=row['sku'],
                price=row['price'],
                discount_price=row.get('discount_price', None),
                stock_quantity=row['stock_quantity'],
                category=category,
                vendor=vendor,
                available=True,
            )
            products.append(product)

        cls.objects.bulk_create(products)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.name} Specification: {self.name}"

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} for {self.product.name}"

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    variant_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    sku = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.variant_name} - {self.product.name}"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.product.name}"

    class Meta:
        unique_together = ['product', 'user']