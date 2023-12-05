
from flask import Flask,request, Response
from joblib import load

#Loading my model

my_lr_model=load('my_lr_model.joblib')
#Initializing
app = Flask(__name__)

#Creating the very first route


@app.route("/get_salary_predictions",methods=['POST','GET'])
def get_salary_predictions():
    data=request.json

    user_sent_this_data=data.get('mydata')
    user_number=float(user_sent_this_data)

    #using the users data and giving it to our model
    model_prediction=my_lr_model.predict([[user_number]])

    #returning the response
    return Response(str(model_prediction))

if __name__=='__main__':
    app.run(debug=True)



