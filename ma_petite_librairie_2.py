# =============================================================================
# Lister le livre écrit par l’auteur « Dr. Kaitlyn Ratke »
# =============================================================================

import requests
payload = {'author':'Dr. Kaitlyn Ratke'}
r = requests.get("https://demo.api-platform.com/books", params = payload)
r = r.json()
r = r["hydra:member"][0]['title']
print('Titre : ', r)