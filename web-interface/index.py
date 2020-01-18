import subprocess
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET"])
def get():
    result = subprocess.run(['helm', 'list', '-o', 'json'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    return jsonify(json.loads(result))


@app.route('/<name>', methods=["DELETE"])
def delete():
    name = request.args.get("name")
    if not name.startswith("git-branch"):
        abort(404)

    result = subprocess.run(["helm", "uninstall", name], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return jsonify(json.loads(result))


