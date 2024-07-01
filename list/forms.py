# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError
#
# from list.models import Tag, Task
#
#
# class TagForm(forms.ModelForm):
#     drivers = forms.ModelMultipleChoiceField(
#         queryset=get_user_model().objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#     )
#
#     class Meta:
#         model = Tag
#         fields = "__all__"
