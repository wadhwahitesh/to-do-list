from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200,required=False)
    check = forms.BooleanField(required=False)


class CreateNewItem(forms.Form):
    text=forms.CharField(label="New Item", max_length=200)

