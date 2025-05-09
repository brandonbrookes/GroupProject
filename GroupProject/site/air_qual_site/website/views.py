from django.shortcuts import render
from .models import AirQuality
from .forms import PostCodeForm
from .utils import get_air_quality_for_postcode

def postCodeLookUp(request):
    data = None
    times, pm1_list, pm2_list, pm3_list = [], [], [], []
    error = None
    selected_postcode = None 
    
    if request.method == 'POST':
        form = PostCodeForm(request.POST)
        if form.is_valid():
            selected_postcode = form.cleaned_data['postcode'].lower()

            data = get_air_quality_for_postcode(selected_postcode)
            
            if data:
                history = AirQuality.objects.filter(postcode=selected_postcode).order_by('date')
                times = [entry.date.strftime('%Y-%m-%d') for entry in history]
                pm1_list = [entry.pm1 for entry in history]
                pm2_list = [entry.pm2 for entry in history]
                pm3_list = [entry.pm3 for entry in history]
            else:
                error = "No air quality data found for that postcode."
    else:
        form = PostCodeForm()

    return render(request, 'postCodeLookUp.html', {
        'form': form,
        'data': data,
        'error': error,
        'times': times,
        'pm1': pm1_list,
        'pm2': pm2_list,
        'pm3': pm3_list,
        'selected_postcode': selected_postcode 
    })
