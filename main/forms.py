from django import forms
from main.models import Product, Contact, Version

EXCLUDED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    """Миксин для стилизации форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ContactForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email',)


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        # fields = ('name', 'is_published', 'description', 'preview', 'category', 'price',)
        exclude = ('owner_product',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in cleaned_data.split():
            if word in EXCLUDED_WORDS:
                raise forms.ValidationError(('%(value)s : запрещенное слово в названии продукта'), code='error1', params={'value': word})
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in cleaned_data.split():
            if word in EXCLUDED_WORDS:
                raise forms.ValidationError(('%(value)s : запрещенное слово в описании продукта'), code='error2', params={'value': word})
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
