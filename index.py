from flask import Flask,request,jsonify
app = Flask(__name__)
from apriori_python import apriori
import core
@app.route("/",methods=["GET","POST"])
def hello_world():
    if(request.method == "POST"):
        resultApriori = []
        getData = request.json.get("data")
        print(getData)
        freqItemSet, rules = apriori(getData, minSup=0.5, minConf=0.5)
        formatted_response = []
        for rule in rules:
            antecedent, consequent, confidence = rule
            formatted_rule = {
                'antecedent': list(antecedent),
                'consequent': list(consequent),
                'confidence': confidence
            }
            formatted_response.append(formatted_rule)
        return jsonify({
            "message":formatted_response
        })
    else:
        return jsonify({
            "message":"this method get"
        })





if __name__ == "__main__":
    app.run(port=3000,debug=True)