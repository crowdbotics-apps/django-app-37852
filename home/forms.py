from django import forms
from .models import App, Plans, Subscription


# creates the form for the app model


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        # gets all fields from the model
        fields = "__all__"

# creates the form for the plan model


class planForm(forms.ModelForm):
    class Meta:
        model = Plans
        # gets all fields from the model
        fields = "__all__"


# creates the form for the subscriptions model
class SubsForm(forms.ModelForm):
    class Meta:
        model = Subscription
        # gets all fields from the model
        fields = "__all__"
