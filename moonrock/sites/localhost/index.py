from flask import Flask, url_for, render_template
app = Flask(__name__)



@app.route('/explore')
def indexblog():
    return render_template('indexblog.html', blog=True)


@app.route('/')
def carousel():
    return render_template('carousel.html', home=True)

@app.route('/checkout/<string:plan>', methods=['GET'])
def checkout(plan):
    price = {'k1': 15, 'k6': 72, 'k12':108}[plan]
    return render_template('checkout.html', checkout=True, plan=plan, price=price)

@app.route('/checkout/<string:plan>', methods=['POST'])
def checkoutpost(plan):
    price = {'k1': 15, 'k6': 72, 'k12':108}[plan]
    return "checkout WORKS"
    return render_template('checkout.html', checkout=True, plan=plan, price=price)

@app.route('/promo/<string:promo>', methods=['POST'])
def promo(promo):
    codes = {'MR10': '10', 'MR5':'5', 'MRHALFPRICE':'50%'}
    return codes[promo]

@app.route('/learn')
def album():
    return render_template('learn.html', learn=True)

@app.route('/subscribe')
def pricing():
    return render_template('pricing.html', subscribe=True)

@app.route('/old')
def old():
    return render_template('oldblogcode.html')