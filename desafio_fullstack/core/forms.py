from django import forms

from desafio_fullstack.core.models import Estado, Cidade


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = '__all__'

    def clean_sigla(self):
        sigla = self.cleaned_data['sigla']
        return sigla.upper()

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.title()

    def __init__(self, *args, **kwargs):
        super(EstadoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.title()

    def __init__(self, *args, **kwargs):
        super(CidadeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
