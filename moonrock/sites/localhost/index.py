from flask import Flask, url_for, render_template
app = Flask(__name__)



@app.route('/')
def hello_world():
    print(url_for('static', filename='style.css'))
    return render_template('indexblog.html')

@app.route('/carousel')
def carousel():
    return render_template('carousel.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')