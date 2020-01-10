# =============================================================================
# API OpenWeatherMap
# =============================================================================

import requests

# Mon API KEY (ne pas en abuser merci)
api_key = 'f59b0dd4f6ec7b67e871e2d48273667a'

#On demande le nom d'une ville en France
city_name = input('Rentrez le nom de votre ville (en France): ')

# On construit l'url
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + ',fr&appid=' + api_key + '&lang=fr'

# On stocke la réponse et on printe le résultat
res = requests.get(url).json()
print("Le temps aujourd'hui à", city_name.upper(), 'est:', res['weather'][0]['description'])
