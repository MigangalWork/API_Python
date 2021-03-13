# Importing Flask and other modules 
from flask import Flask, request, render_template  
from writingData import update_json

# Flask constructor 
app = Flask(__name__)    

# A decorator used to tell the application 
# which URL is associated function 

@app.route('/', methods =['GET', 'POST'])

def gfg(): 
   if request.method == 'POST':
      user = request.form.get('user')
      password = request.form.get('pw')

      new_data = [user, password]
      update_json('register.json', new_data)
      return 'Se ha registrado correctamente'
   return render_template('index.html')


if __name__=='__main__': 
   app.run()