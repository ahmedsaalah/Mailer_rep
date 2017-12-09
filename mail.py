from flask import Flask
from flask_mail import Mail, Message
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
import hashlib
from usermodel import usermodel

from flask import session as login_session


import requests
import json
app =Flask(__name__)
mail=Mail(app)
app.secret_key = 'some_secret'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'eng.ahmad.abobakr@gmail.com'
app.config['MAIL_PASSWORD'] = 'kramara1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
''' Views  '''
@app.route('/')
def HomePage():
    active = "SendMail"
    return render_template('imo.html' ,message="")



@app.route('/send')
def routeToMain():
    res = checkToRediect()
    if res :
        active = "SendMail"
        return render_template('SendMail.html' ,active=active ,message="")
    else :
        return redirect(url_for('HomePage'))
        
@app.route('/addToList')
def addToList(message = ''):
    
    res = checkToRediect()
    if res :
        active = "AddtoList"

        return render_template('addToList.html' ,active=active ,message="")

    else :
        return redirect(url_for('HomePage'))
    


''' end Views  '''




''' post request  function  '''
@app.route("/login", methods=['POST','GET'])
def login():
    email = request.form["email"]
    password = request.form["pass"]

    user = usermodel()
    response = user.getifExist(email,haaash(password))
    if response :
        login_session['state'] = email
        return redirect(url_for('routeToMain'))
    else :
        message = alertFunc("the email address and password you entered  not matched")
        return render_template('signin.html' ,message= message)

    


@app.route("/logout", methods=['POST','GET'])
def logout():
    
    del login_session['state']
    return redirect(url_for('HomePage'))
    
    

@app.route("/SendMAIL", methods=['POST','GET'])
def sendmail():
   

    msg = request.form["msgpost"]
    print(msg)
    
        

    return render_template('imo.html' ,message=msg ,msg=msg)
    # return redirect(url_for('routeToMain'))



@app.route("/add", methods=['POST','GET'])
def add_list_member():
    

    email = request.form["email"]
    
    r = requests.post(
        "https://api.mailgun.net/v3/lists/best@bestofferz.top/members",
        auth=('api', 'key-9b0f9477e53b446adf19f1371d809aef'),
        data={'subscribed': True,
              'address': email
              })

    login_session['message'] =  "Email added successfully to list"
    return redirect(url_for('addToList'))
    



''' end post request  function  '''

''' main function '''

@app.route("/complex_Send")
def send_email(mailContent, subject):

    MAILGUN_API_KEY = "key-8cafc2ea8c8b2b14a329173afe11c325"
    
    to = 'ahmode2003@gmail.com'
    
    f ="mr.Younis <postmaster@bestofferz.top>"
    url = "https://api.mailgun.net/v3/sandbox727fec112f48401bacea21224c2846cd.mailgun.org/messages"
    auth = ('api', MAILGUN_API_KEY)
    data = {
        'from': f,
        'to': to,
        'subject': subject,
        'text': 'Plaintext content',
        'html': mailContent
    
    }
    

    response = requests.post(url, auth=auth, data=data)
    return response.text


''' end main function '''


def alertFunc(Message):
    return "<script>alert('"+Message+"')</script>"

    

def haaash(w):
    
    h = hashlib.sha256(w)
    return h.digest().encode('base64')[:6]



def checkToRediect():
    try:
        if  login_session['state'] == "younesidbs@gmail.com" :
            return True
        else :
            return False
          

        
    except KeyError:
        return False



@app.template_filter('ses')
def _ses(string=""):
    try:
        if  login_session['message'] == "" :
            pass
        elif login_session['message'] :
            
            string = login_session['message']
            string =alertFunc(string)

        
            del login_session['message']

        
    except KeyError:
        pass


    return string






''' end'''



if __name__ == '__main__':
   app.run(debug = True)