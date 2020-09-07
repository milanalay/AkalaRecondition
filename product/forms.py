from django import forms

from product.models.datamodel import Incoming, Outgoing
from product.models.expendituremodel import Expenditure


class DateInput(forms.DateInput):
    input_type = 'date'


class IncomingForm(forms.ModelForm):
    image = forms.ImageField()
    date = forms.DateField(widget=DateInput)
    def __init__(self, *args, **kwargs):
        super(IncomingForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Eg: KTM Duke 390',
            'class': 'form-control',
        })
        self.fields['model'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['bike_number'].widget.attrs.update({
            'placeholder': 'Eg: Ga 12 Pa xxxx',
            'class': 'form-control',
        })
        self.fields['price'].widget.attrs.update({
            'placeholder': 'Rs.',
            'class': 'form-control',
        })
        self.fields['sale_price'].widget.attrs.update({
            'placeholder': 'Rs.',
            'class': 'form-control',
        })
        self.fields['owner'].widget.attrs.update({
            'placeholder': 'Eg: Dave Mustaine',
            'class': 'form-control',
        })
        self.fields['contact'].widget.attrs.update({
            'placeholder': 'Eg: 98xxxxxxxx',
            'class': 'form-control',
        })
        self.fields['date'].widget.attrs.update({
                'class': 'form-control'
            })
        # for field in self.fields.keys():
        #     self.fields[field].widget.attrs.update({
        #         'class': 'form-control',
        #     })
        


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
    date = forms.DateField(widget=DateInput)

    def __init__(self, *args, **kwargs):
        super(OutgoingForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Incoming.objects.filter(stock='Available')
        self.fields['price'].widget.attrs.update({
            'placeholder': 'Rs.'
        })
        self.fields['customer'].widget.attrs.update({
            'placeholder': 'Eg: James Hetfield'
        })
        self.fields['contact'].widget.attrs.update({
            'placeholder': 'Eg: 98xxxxxxxx'
        })
        self.fields['date'].widget.attrs.update({
            'class': 'form-control'
        })
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })



    class Meta:
        model = Outgoing
        fields = '__all__'



class ExpenditureForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    def __init__(self, *args, **kwargs):
        super(ExpenditureForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'placeholder': 'Eg: Rent'
        })
        self.fields['amount'].widget.attrs.update({
            'placeholder': 'Rs.'
        })
        self.fields['date'].widget.attrs.update({
            'class': 'form-control'
        })

        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Expenditure
        fields = '__all__'