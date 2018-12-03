from flask import Flask, request, Response
from werkzeug import secure_filename
import json

app = Flask(__name__)

@app.route('/fileName', methods=['POST'])
def getfileName():
    r = request.json
    print(r['key'])
    return "success send file Name"

@app.route('/fileUpload', methods=['POST'])
def getfileUpload():
    f = request.files['file']
    f.save('privateRepository/'+secure_filename(f.filename))
    return "success send uploaded file"

# start flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
