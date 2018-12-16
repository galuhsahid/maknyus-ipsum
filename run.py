from flask import Flask, render_template, jsonify, request
from random import *
from flask_cors import CORS
import requests
from makanan import makanan 
from random import sample 
from random import randrange 
import re

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

middle_puncts = set([",", ";"])
end_puncts = set(["?", "!", "."])

def build_sentence():
    sentence = sample(makanan, randrange(5, 7))
    punct = sample(middle_puncts, randrange(0,3))
    
    for pun in punct:
        while True:
            rand_pos = randrange(1, len(sentence)-1)
            if ((sentence[rand_pos-1] not in middle_puncts)
            and (sentence[rand_pos] not in middle_puncts)):
                sentence.insert(rand_pos, pun)
                break

    sentence[len(sentence)-1] = sample(end_puncts, 1)[0]
    sentence = ' '.join(sentence)
    sentence = str.capitalize(sentence)
    sentence = re.sub(r' (?=\W)', '', sentence)
    
    return sentence

def build_paragraph():
    sentence = randrange(3, 10)
    paragraph = []

    for x in range(0, sentence):
        paragraph.append(build_sentence())

    return ' '.join(paragraph)

def build_text(paragraphs_num):
    text = []

    for x in range(0, paragraphs_num):
        text.append(build_paragraph())
    
    return '\n\n'.join(text)

@app.route('/api/maknyus', methods=['GET'])
def maknyus():
    paragraphs_num = int(request.args.get('n'))
    response = {
        'text': build_text(paragraphs_num)
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
