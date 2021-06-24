from django import forms


class CreateList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    # completed = forms.BooleanField(label="Completed?", required=False)
    # This means that it is not necessary to check the box if required = False
