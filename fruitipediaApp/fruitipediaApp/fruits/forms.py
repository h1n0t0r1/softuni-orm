from django import forms

from .models import Category, Fruit


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class CategoryForm(CategoryBaseForm):
    pass


class FruitAddForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    pass


class DeleteFruitForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True