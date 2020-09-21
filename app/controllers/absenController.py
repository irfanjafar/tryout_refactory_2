from app.model.absen import Absens
from flask import request, jsonify
from app import response, db
from app.controllers import userController, kelasController
from flask_jwt_extended import *

@jwt_required
def store():
    try:
        description = request.json['description']
        user_id = request.json['user_id']
        kelas_id = request.json['kelas_id']

        absen = Absens(user_id=user_id, kelas_id=kelas_id, description=description)
        db.session.add(absen)
        db.session.commit()

        return response.ok('', 'Successfully create absen!')

    except Exception as e:
        print(e)

@jwt_required
def index():
    try:
        absens = Absens.query.all()
        data = transform(absens)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values):
    data = {
        'id': values.id,
        'user_id': values.user_id,
        'kelas_id': values.kelas_id,
        'description': values.description,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
    }
    return data


@jwt_required
def update(id):
    try:
        inputDescription = request.json['description']
        inputUser_id = request.json['user_id']
        inputKelas_id = request.json['kelas_id']
        absen = Absens.query.filter_by(id=id).first()
        
        absen.description = inputDescription
        absen.user_id = inputUser_id
        absen.kelas_id = inputKelas_id
        db.session.commit()
        return response.ok('', 'Successfully update absen!')
    except Exception as e:
        print(e)

@jwt_required
def show(id):
    try:
        absen = Absens.query.filter_by(id=id).first()
        if not absen:
            return response.badRequest([], 'Empty....')

        data = singleTransform(absen)
        return response.ok(data, "")
    except Exception as e:
        print(e)




