import requests

r=requests.get('http://127.0.0.1:5000/testing',json={"mydata":'1'})

r.status_code
r.text

