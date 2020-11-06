from flask import Flask, url_for, render_template
app = Flask(__name__)



@app.route('/explore')
def indexblog():
    return render_template('indexblog.html')


@app.route('/')
def carousel():
    return render_template('carousel.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/learn')
def album():
    return render_template('learn.tpl')

@app.route('/subscribe')
def pricing():
    return render_template('pricing.html')
