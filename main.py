from flask import Flask

#Initializing
app = Flask(__name__)

#Creating the very first route
@app.route("/greetings")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/help")
def help():
    return "<p>Help me</p>"

if __name__=='__main__':
    app.run(debug=True)






