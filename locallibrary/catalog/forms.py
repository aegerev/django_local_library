from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import datetime

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 1 month from now. ")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_("We don't think about the past. We think about the present and focus on the future." ))
        elif data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_("While we think about the future, we can't time travel. Sorry."))
        
        return data
