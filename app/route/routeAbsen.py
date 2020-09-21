from app import app
from app.controllers import absenController
from flask import request


@app.route('/absen', methods=['POST', 'GET'])
def absens():
    if request.method == 'GET':
        return absenController.index()
    else:
        return absenController.store()

@app.route('/absen/', methods=['PUT', 'GET'])
@app.route('/absen/<id>', methods=['PUT', 'GET'])
def absensDetail(id=0):
    if request.method == 'GET':
        return absenController.show(id)
    elif request.method == 'PUT':
        return absenController.update(id)
