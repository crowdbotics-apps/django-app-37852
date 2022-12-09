from django import forms  
from .models import  App,Plans ,Subscription 

class AppForm(forms.ModelForm):  
    class Meta:  
        model = App  
       
        fields = "__all__" 

class planForm(forms.ModelForm):  
    class Meta:  
        model = Plans  
       
        fields = "__all__" 


class SubsForm(forms.ModelForm):  
    class Meta:  
        model = Subscription  
       
        fields = "__all__" 