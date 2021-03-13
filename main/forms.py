from django import forms

class Record(forms.Form):
    name= forms.CharField(label= "Name")
    std= forms.IntegerField(label="Class")
    board= forms.CharField(label= "Board")