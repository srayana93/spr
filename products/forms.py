from django import forms
from .models import Product, ProductImage, ProductSpecification, ProductAttribute, ProductVariant
from categories.models import Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'slug', 'sku', 'price', 
            'discount_price', 'stock_quantity', 'available', 
            'category'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Product.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Slug must be unique.")
        return slug

    def save(self, commit=True):
        product = super().save(commit=False)
        product.vendor = self.initial['vendor']
        if commit:
            product.save()
        return product

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']

class ProductSpecificationForm(forms.ModelForm):
    class Meta:
        model = ProductSpecification
        fields = ['name', 'value']

class ProductAttributeForm(forms.ModelForm):
    class Meta:
        model = ProductAttribute
        fields = ['name', 'value']

class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['variant_name', 'price', 'stock_quantity', 'sku']

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()

    def clean_csv_file(self):
        file = self.cleaned_data['csv_file']
        if not file.name.endswith('.csv'):
            raise forms.ValidationError("The file must be a CSV.")
        return file