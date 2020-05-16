#from wsgiref.simple_server import make_server
# https://uwsgi-docs.readthedocs.io/en/latest/Python.html


from flask import Flask, render_template, flash, url_for, redirect, request
from forms import Adjust
import driver

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c1c2d54334c8b961518f45c99e506a76'

#address: 192.168.1.70:9090/home

driver1 = driver.Driver()

@app.route("/")
def base():
    return "IP:192.168.1.70 Port:9090"
    
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/drive", methods=['GET', 'POST'])
# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask

def adjust():
    form = Adjust()
    if form.validate_on_submit():
        flash('Speed Set at %s' % form.speed.data , 'success')
        print(form.speed.data, type(form.speed.data))
        driver1.setSpeed(form.speed.data)

    if(request.get_json() != None):
        req_data = request.get_json()
        operation = req_data['Operation']
        print('Operation: ', operation)
        if( operation == 'Forward'):
            flash('Moving PiBot Forward', 'success')
            print('Moving Pi Bot Forward')
            driver1.Forward()

        elif( operation == 'Backward'):
            flash('Moving PiBot Backward', 'success')
            print('Moving Pi Bot Backward') 
            driver1.Backward()     

        elif( operation == 'Left'):
            flash('Steering PiBot Left', 'success')
            print('Stering Pi Bot Left')
            driver1.Left()      

        elif( operation == 'Right'):
            flash('Steering PiBot Right', 'success')
            print('Stearing Pi Bot Right')
            driver1.Right()      

        elif( operation == 'Stop' ):
            driver1.Stop()


    return render_template('drive.html', title='Drive PiBot', form=form)



@app.route("/joystick", methods=['GET', 'POST'])
def joystick():
    return render_template('joystick.html', title='Joystick')


print("Name is %s " % __name__)
if ( (__name__ == '__main__') ) :
    app.run(debug=True)
