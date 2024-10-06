from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
import os

load_dotenv() # Pour permettre au script d'accéder aux variable environnement du fichier '.env'
app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY') # Fournir la clé API à la fonction api_key de openai

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST": # Vérifier si un prompt est envoyé
        prompt = request.form.get('prompt') # Récuperer le texte du prompt
        # Renvoyer le prompt à openai
        response = openai.Image.create(
            prompt=prompt,
            n=1, # Nombre d'images à generées
            size="1024x1024" # Taille de l'image
        )
        image_url = response['data'][0]['url'] # Récuperer le lien des images generées
        if image_url:
            return render_template('index.html', image_url=image_url, prompt=prompt)
        else:
            return render_template('index.html', error="")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
