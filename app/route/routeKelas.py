from app import app
from app.controllers import kelasController
from flask import request


@app.route('/kelas', methods=['POST', 'GET'])
def kelass():
    if request.method == 'GET':
        return kelasController.index()
    else:
        return kelasController.store()


@app.route('/kelas/', methods=['PUT', 'GET', 'DELETE'])
@app.route('/kelas/<id>', methods=['PUT', 'GET', 'DELETE'])
def kelassDetail(id=0):
    if request.method == 'GET':
        return kelasController.show(id)
    elif request.method == 'PUT':
        return kelasController.update(id)
    elif request.method == 'DELETE':
        return kelasController.delete(id)

