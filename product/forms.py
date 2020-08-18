from django import forms

from product.models.datamodel import Incoming, Outgoing
from product.models.expendituremodel import Expenditure





class IncomingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IncomingForm, self).__init__(*args, **kwargs)
        
        self.fields['date'].widget.attrs.update({
                'placeholder': 'mm/dd/yyyy',
                'input_formats': '%m/%d/%Y',
                'class': 'form-control datetimepicker-input'
            })
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
        


    class Meta:
        model = Incoming
        fields = '__all__'
        exclude = ('slug', 'stock', 'sanakhat', 'passed', )


class IncomingUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(IncomingUpdateForm, self).__init__(*args, **kwargs)

        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Incoming
        fields = '__all__'
        exclude = ('slug', 'stock', 'date',)



class OutgoingForm(forms.ModelForm):
    date = forms.DateField(input_formats = ['%m/%d/%Y',])

    def __init__(self, *args, **kwargs):
        super(OutgoingForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Incoming.objects.filter(stock='Available')
        self.fields['date'].widget.attrs.update({
            'placeholder': 'mm/dd/yyyy',
            'class': 'form-control datetimepicker-input'
        })
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })



    class Meta:
        model = Outgoing
        fields = '__all__'



class ExpenditureForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExpenditureForm, self).__init__(*args, **kwargs)

        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Expenditure
        fields = '__all__'