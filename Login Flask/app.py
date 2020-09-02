from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'Parth':'123','Surender':'12abc','bcfg':'asdsf'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    butt=request.form['submit']
    if butt=='login':
       if name1 not in database:
           return render_template('login.html',info='Register As New User') 
          
       elif database[name1]!=pwd:
              return render_template('login.html',info='Invalid Password')
       else:
              return render_template('home.html',name=name1)
    elif butt=='signup':
       if name1 not in database:
           database[name1]=pwd
           return render_template('login.html',info='Registered As New User')
       else:
           if database[name1]!=pwd:
               database[name1]=pwd
               return render_template('login.html',info='Password Changed')
           if database[name1]==pwd:
               return render_template('login.html',info='Same Password Entered')
        
              
if __name__ == '__main__':
    app.run()
