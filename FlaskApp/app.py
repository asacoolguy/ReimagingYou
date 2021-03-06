from flask import Flask, render_template, send_file, url_for
from wordcloud import WordCloud
import StringIO
from os import path
from PIL import Image
import numpy as np

COLOR_RED = '#FF0000'
COLOR_BLUE = '#0000FF'
COLOR_GREEN = '#1A7E55'
COLOR_PURPLE = '#6617B5'


app = Flask(__name__)
d = path.dirname(__file__)

@app.route("/")
def main():
    return render_template(
        'index.html',
        title = 'yay word clouds!',
        pic = url_for('generateWordCloud'))

@app.route("/generate/")
def generateWordCloud():
    words_old = [  #some words to visualize
        { 
            'word': 'this', 
            'size': 55,
            'color': COLOR_RED,
            'font': '\'Indie Flower\', cursive',
            'angle': '45'
        },
        { 
            'word': 'Test', 
            'size': 73,
            'color': COLOR_BLUE,
            'font': '\'Open Sans\', sans-serif',
            'angle': '-30'
        },
        { 
            'word': 'kinDA', 
            'size': 153,
            'color': COLOR_GREEN,
            'font': '\'Indie Flower\', cursive',
            'angle': '-150'
        },
        { 
            'word': 'WERKS', 
            'size': 33,
            'color': COLOR_PURPLE,
            'font': '\'Open Sans\', sans-serif',
            'angle': '90'
        }
    ]

    # Read the whole text.
    words = [('chipotle', 55), ('McDonalds', 15), ('burgerking', 12), ('wendies', 41), ('using', 1), ('font', 2), ('randomize', 1), ('yet', 1), ('HHBs', 1), ('knowledge', 1), ('generator', 1), ('everything', 3), ('implementation', 2), ('simple', 2), ('might', 1), ('pixel', 1), ('real', 1), ('designs', 1), ('good', 1), ('without', 1), ('checking', 1), ('trees', 2), ('famous', 1), ('boxes', 1), ('every', 1), ('optimal', 1), ('front', 1), ('integer', 1), ('bit', 2), ('now', 2), ('easily', 1), ('shape', 1), ('fs', 1), ('stuff', 1), ('found', 1), ('works', 1), ('view', 1), ('right', 1), ('force', 1), ('generation', 3), ('hard', 1), ('back', 1), ('second', 1), ('sure', 1), ('Hopefully', 1), ('portrait', 1), ('best', 1), ('really', 2), ('speed', 1), ('method', 2), ('dataset', 2), ('figuring', 1), ('modify', 1), ('understanding', 1), ('represented', 1), ('come', 1), ('generate', 2), ('last', 2), ('fit', 1), ('Tweak', 1), ('study', 1), ('studied', 1), ('turn', 1), ('place', 2), ('isn', 1), ('uses', 2), ('implement', 1), ('sprites', 1), ('adjustable', 1), ('render', 1), ('color', 2), ('one', 1), ('fashion', 1), ('fake', 1), ('cloud', 5), ('size', 2), ('guess', 1), ('working', 1), ('Separate', 1), ('sake', 1), ('placing', 1), ('brute', 1), ('least', 2), ('insider', 1), ('lot', 1), ('basic', 1), ('prototype', 1), ('start', 1), ('empty', 1), ('sort', 1), ('testing', 1), ('spiral', 1), ('overlapping', 1), ('else', 1), ('controller', 1), ('part', 2), ('somewhat', 1), ('varying', 1), ('MySQL', 1), ('quad', 2), ('copy', 1), ('also', 1), ('bundled', 1), ('word', 9), ('algorithm', 2), ('typography', 1), ('will', 1), ('fll', 1), ('following', 2), ('bet', 1), ('perfecting', 1), ('proved', 1), ('orientation', 2), ('wordle', 1), ('JavaScript', 1), ('collision', 2), ('reads', 1), ('want', 1), ('ready', 1), ('compressing', 1), ('apparently', 1), ('check', 1), ('inefficient', 1), ('preferably', 1), ('end', 2), ('thing', 2), ('efficient', 1), ('make', 3), ('note', 1), ('python', 3), ('need', 3), ('complex', 1), ('instead', 1), ('hierarchical', 1), ('used', 1), ('ft', 1), ('see', 1), ('though', 2), ('moving', 1), ('preliminary', 1), ('data', 1), ('fm', 1), ('Figure', 2), ('database', 1), ('author', 1), ('together', 1), ('think', 1), ('provide', 1), ('definitely', 1), ('time', 1), ('position', 2), ('model', 2), ('D3', 1)]
    
    alice_mask = np.array(Image.open(path.join(d,"alice_mask.png")))
    burrito_mask = np.array(Image.open(path.join(d,"burrito2.png")))

    print alice_mask.shape
    print burrito_mask.shape

    # Generate a word cloud image
    wordcloud = WordCloud(
        background_color="white",
        max_words = 1500,
        mask = burrito_mask)
    wordcloud.generate_from_frequencies(words)

    # The pil way (if you don't have matplotlib)
    image = wordcloud.to_image()
    #words = wordcloud.process_text(text)
    #image.show()

    return serveImg(image)

def serveImg(img):
    img_io = StringIO.StringIO()
    img.save(img_io,"JPEG")
    img_io.seek(0);\
    return send_file(img_io,mimetype='image/jpeg')


if __name__ == "__main__":
    app.run(debug=True)
