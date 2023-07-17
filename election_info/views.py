from django.shortcuts import render
from .models import Polling_unit, Lga
from .forms import PuResultsCreationForm


def homepage(request):
    return render(request, 'homepage.html')


def display_result(request):
    polling_units = Polling_unit.objects.all()
    pu_result = []
    for each in polling_units:
        pu_result = each.polling_unit_uniqid.all()
    context = {
        'pu_result': pu_result
    }
    return render(request, 'display_results.html', context)


def sum_pu_lga(request):
    lga = Lga.objects.all()
    lga_names = []
    lga_polling_units = ''
    for each in lga:
        lga_names.append(each.lga_name)
        lga_polling_units = Polling_unit.objects.get(lga_id=each.id)
    summed = 0
    for each in lga_polling_units:
        summed += each.polling_unit_uniqid.party_score
    context = {
        'lga_names': lga_names,
        'summed': summed
    }
    return render(request, 'sum_total.html', context)


def store_results(request):
    form = PuResultsCreationForm()
    if request.method == 'POST':
        form = PuResultsCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'store_results.html', context)

