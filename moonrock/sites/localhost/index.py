from flask import Flask, url_for, render_template
app = Flask(__name__)



@app.route('/explore')
def indexblog():
    return render_template('indexblog.html', blog=True)


@app.route('/')
def carousel():
    return render_template('carousel.html', home=True)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/learn')
def album():
    return render_template('learn.tpl')

@app.route('/subscribe')
def pricing():
    return render_template('pricing.html')

@app.route('/old')
def old():
    return render_template('oldblogcode.html')