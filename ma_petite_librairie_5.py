# =============================================================================
# Modifier votre nouveau commentaire en utilisant l’id qui vous a été fourni lors de sa création
# =============================================================================
import requests
import json

myCommentId = '/reviews/27b081d7-f201-4af2-9184-ce02c14cec6f'
print('id de mon commentaire : ',myCommentId)

url = f'https://demo.api-platform.com' + myCommentId

body = {"body": "Lire le Sud-Ouest est beaucoup plus palpitant que votre livre"}

headers = {'Content-Type': 'application/merge-patch+json'}

r = requests.patch(url, headers=headers, data=json.dumps(body))
print('Mon commentaire modifié:',r.json()['body'])