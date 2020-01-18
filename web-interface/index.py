import subprocess
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET"])
def get():
    result = subprocess.run(['helm', 'list', '-o', 'json'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    result_json = json.loads(result)
    output_dict = [x for x in result_json if x['name'].startswith("git-branch")]

    return json.dumps(output_dict)


@app.route('/', methods=["DELETE"])
def delete():
    name = request.args.get("name")
    print(name)
    if not name.startswith("git-branch"):
        abort(404)

    subprocess.run(["helm", "uninstall", name], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


