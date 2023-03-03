from flask import Flask, request
import pandas

app = Flask(__name__)

@app.route('/')
def Index():
    return 'Irregualr Verbs API By Mr. mohammed Radwan'

@app.get('/GetP')
def GetParticiples():
    srch = request.args.get('srch')
    df = pandas.read_csv("db.csv")
    result = df.loc[df['Infinitive'] == srch]
    return result.to_json(orient="records")

if __name__ == "__main__":
    app.run(host="0.0.0.0")





