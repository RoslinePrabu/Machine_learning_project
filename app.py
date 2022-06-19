from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "CID CD Pipeline has been established"

if __name__=="__main__":
    app.run(debug=True)