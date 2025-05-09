#import requests
from .models import AirQuality

def get_air_quality_for_postcode(postcode):
    #normalise
    postcode = postcode.strip().upper()

    try:
        # get most recent air qual data for that postcode
        data = AirQuality.objects.filter(postcode=postcode).latest('date')

        pm_values = {
            'PM1': data.pm1,
            'PM2': data.pm2,
            'PM3': data.pm3,
        }
        main_pollutant = max(pm_values, key=pm_values.get)
        return {
            'pm1': data.pm1,
            'pm2': data.pm2,
            'pm3': data.pm3,
            'time': data.date,
            'postcode': data.postcode,
            'pollutant': main_pollutant
        }
    except AirQuality.DoesNotExist:
        return None