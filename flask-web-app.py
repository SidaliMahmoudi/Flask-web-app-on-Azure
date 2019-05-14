from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Testing deployement flask app on azure"

if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)