# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#from flask import Flask
from bardapi import Bard
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bardapi/speech')
def speech():
    bard = Bard(token='YgjdenmnVllP0049BbUVYL7_U8yPtf34t76GZNAqfrisYEUEkA4so6W30BHZpBPyFdGmhQ.')
    audio = bard.speech("Xin chào, bạn tên là gì?", lang='vi-VN')  # Get bytes audio object.

    # Save audio object.
    with open('bard_response.mp3', 'wb') as f:
        f.write(audio)
    return 'Hello, World!'

@app.route('/bardapi/',methods=('POST',))
def get_answer():
    data = request.get_json()
    question = data.get("question","")

    #question = "Quán massage chổ nào gần đây？";
    bard = Bard(token='YgjdenmnVllP0049BbUVYL7_U8yPtf34t76GZNAqfrisYEUEkA4so6W30BHZpBPyFdGmhQ.', language='vietnamese')
    res = bard.get_answer(question)
    #print(res['content'])

    return res

@app.route('/')
def hello():
    return 'Hello, World!'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
