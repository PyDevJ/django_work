from django import forms
from main.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'preview', 'category', 'price',)
        # exclude = ('created_at', 'changed_at',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if 'казино' in cleaned_data:
            raise forms.ValidationError('Нельзя применять это наименование')

        return cleaned_data

    # def clean_description(self):
    #     cleaned_data = self.cleaned_data['description']
    #
    #     if 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'дешево' or 'бесплатно' or 'обман' or 'полиция' or 'радар' in cleaned_data:
    #         raise forms.ValidationError('Нельзя применять это описание')
    #
    #     return cleaned_data
