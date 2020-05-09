#from wsgiref.simple_server import make_server
# https://uwsgi-docs.readthedocs.io/en/latest/Python.html


from flask import Flask, render_template, flash, url_for, redirect
from forms import Adjust

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c1c2d54334c8b961518f45c99e506a76'

#address: 192.168.1.70:9090

#bridge = Bridge()

@app.route("/")
def base():
    return "IP:192.168.1.70 Port:9090"
    
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/drive", methods=['GET', 'POST'])
def adjust():
    form = Adjust()
    if form.validate_on_submit():
        flash('Speed Set at %s' % form.speed.data , 'success')
        #bridge.adjustDuty(form.pwm.data)
        #bridge.adjustFrequency(form.frequency.data)
        
    return render_template('drive.html', title='Drive PiBot', form=form)



print("Name is %s " % __name__)
if ( (__name__ == '__main__') ) :
    app.run(debug=True)
