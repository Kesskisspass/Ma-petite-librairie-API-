# =============================================================================
# Lister tous les commentaires du livre dont l’id est « 1d52ba85-97c8-4cc3-b81a-40582f3aff64 »
# =============================================================================
import requests
r = requests.get('https://demo.api-platform.com/books/1d52ba85-97c8-4cc3-b81a-40582f3aff64/reviews')
r = r.json()['hydra:member']
r
for review in r:
    print('Commentaire : ',review['body'], ' ; Note : ', review['rating'])
    