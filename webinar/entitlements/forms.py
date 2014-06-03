# 2014.06.03 13:21:05 EDT
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.06.03 13:21:05 EDT
