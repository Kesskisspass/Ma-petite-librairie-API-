# =============================================================================
# Créer un nouveau commentaire avec le texte et la note de votre choix pour le livre dont l’id est « 1b08c9ab-6254-4015-ad14-bac3e5c008df »
# =============================================================================
import requests
import json
body = {
  "body": "Lire le Sud-Ouest est plus palpitant que votre livre",
  "rating": 1,
  "author": "Jean Neymar",
  "publicationDate": "2020-01-09T15:08:52.906Z",
  "book" :"/books/1b08c9ab-6254-4015-ad14-bac3e5c008df"
}

headers = {'Content-Type': 'application/json'}

r = requests.post('https://demo.api-platform.com/reviews', headers=headers, data=json.dumps(body))
print(r.json())