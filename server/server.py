from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/fileName', methods=['POST'])
def getfileName():
    r = request.json
    print(r['key'])
    return "success"

# start flask app
if __name__ == '__main__':
    ## To Do####

    

    ############
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
