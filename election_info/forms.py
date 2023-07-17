from django.forms import ModelForm
from .models import Announced_pu_results


class PuResultsCreationForm(ModelForm):
    class Meta:
        model = Announced_pu_results
        fields = ['party_abbreviation', 'party_score', 'entered_by_user']

