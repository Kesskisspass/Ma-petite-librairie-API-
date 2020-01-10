# =============================================================================
# Lister les 10 derniers livres par leur date de publication
# =============================================================================

# On importe le package permettant de faire des requêtes : requests
import requests

# On crée notre url de requête on stocke le resultat dans une variable
r = requests.get("https://demo.api-platform.com/books?order%5BpublicationDate%5D=desc")
# On interprête le résultat reçu en json
r = r.json()
# On extrait du résultat, la partie qui nous intéresse (à savoir les dix premiers)
r = r['hydra:member'][:10]
# On boucle sur chacun des livres pour afficher le titre et la date de publication
for book in r:
    print(book['title'],'publié le : ', book['publicationDate'])
    