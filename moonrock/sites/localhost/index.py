from datetime import date

from flask import Flask, request, url_for, render_template

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
    ccdate = '{}-{}'.format(date.today().year, date.today().month)
    return render_template('checkout.html', 
                           checkout=True, plan=plan, price=price,
                           ccdate=ccdate)

@app.route('/checkout/<string:plan>', methods=['POST'])
def checkoutpost(plan):
    if plan not in ('k1', 'k6', 'k12'):
        exit()
    ccnumber = request.form['ccnumber']
    nameoncard = request.form['ccnameoncard'].upper()
    fullname = request.form['firstname'] + ' ' + request.form['lastname']
    if ccnumber != '1111111111111' or nameoncard != 'JOHN GALT':
        return render_template('errorcard.html', fullname=fullname)
    product = 'MoonRock Kit ' + plan[1:]
    total = request.form['total']
    return render_template('thankyou.html', fullname=fullname,
                             total=total, product=product)

@app.route('/promo/<string:promo>', methods=['POST'])
def promo(promo):
    codes = {'MR10': '10', 'MR5':'5', 'MRHALFPRICE':'50%'}
    if promo in codes:
        return codes[promo]
    else:
        return 'N/A'

@app.route('/learn')
def album():
    return render_template('learn.html', learn=True)

@app.route('/subscribe')
def pricing():
    return render_template('pricing.html', subscribe=True)

@app.route('/old')
def old():
    return render_template('oldblogcode.html')