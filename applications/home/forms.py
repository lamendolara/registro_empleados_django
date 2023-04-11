from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aquí',
                }
            )
        }

    def clean_cantidad(self):
        """Lo mas correcto es hacer este tipo de validaciones para evitar que se guarde en BD
        y el código es más óptimo"""
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un número mayor a 10')

        return cantidad

