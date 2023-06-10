# from django import forms
# from django.forms import ModelForm
# from django.forms import PasswordInput,EmailInput,TextInput,NumberInput
# from main_app.models import Person

# # class PersonForm(forms.Form):
# #     first_name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control'}))
# #     last_name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control'})) 
# #     age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
# #     email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
# #     password=forms.CharField(max_length=15,widget=forms.PasswordInput(attrs={'class':'form-control'}))

# class PersonForm(ModelForm):
#     class Meta:
#         model=Person
#         fields='__all__'
#         widgets={
#             'password':PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
#             'email':EmailInput(attrs={'class':'form-control'}),
#             'first_name':TextInput(attrs={'class':'form-control'}),
#             'last_name':TextInput(attrs={'class':'form-control'}),
#             'age':NumberInput(attrs={'class':'form-control'})

#         }

