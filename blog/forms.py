from django import forms

# определяем класс который наследуется от Form, 
# который определяет поля с валидацией для отправки форм (в данному случае эл.почты)
class EmailPostForms(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
