from flask import Flask
import pandas

app = Flask(__name__)

@app.route('/')
def Index():
    return "Irregualr Verbs API By Mr. mohammed Radwan"

# df = pandas.read_csv("db.csv")
# result = df.loc[df['Infinitive'] == 'be']
# print(result.to_json())

if (__name__ == '__name__'):
    app.run()


