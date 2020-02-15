import sys
from datetime import date
from astral.geocoder import database, lookup
from astral.sun import sun
city_name = sys.argv[1]
city = lookup(city_name, database())
print('Information for %s/%s\n' % (city.name, city.region))
timezone = city.timezone
print('Timezone: %s' % timezone)
print('Latitude: %.02f; Longitude: %.02f\n' % (city.latitude, city.longitude))
s = sun(city.observer, date=date.today())
print('Dawn:    %s' % str(localize(s['dawn'])))
print('Sunrise: %s' % str(s['sunrise']))
print('Noon:    %s' % str(s['noon']))
print('Sunset:  %s' % str(s['sunset']))
print('Dusk:    %s' % str(s['dusk']))
