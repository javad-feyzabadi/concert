from django import forms
from . models import ConsertModel
class SearchForm(forms.Form):
    searchtext = forms.CharField(max_length=100,label='Concert Name' ,required=False)

class ConsertEditForm(forms.ModelForm):
    class  Meta:
        model = ConsertModel
        fields = ['name','singername','length','poster']
        #exclude = ['poster']

class ConsertCreateForm(forms.ModelForm):
    class Meta:
        model = ConsertModel
        fields = ['name','singername','length','poster']
        