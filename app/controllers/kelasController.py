from app.model.kelas import Kelass
from flask import request, jsonify
from app import response, db, app
from flask_jwt_extended import *

@jwt_required
def store():
    try:
        nama_kelas = request.json['nama_kelas']
        nama_pengajar = request.json['nama_pengajar']

        kelas = Kelass(nama_kelas=nama_kelas, nama_pengajar=nama_pengajar)
        db.session.add(kelas)
        db.session.commit()

        return response.ok('', 'Successfully create kelas!')

    except Exception as e:
        print(e)

@jwt_required
def index():
    try:
        kelass = Kelass.query.all()
        data = transform(kelass)
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
        'nama_kelas': values.nama_kelas,
        'nama_pengajar': values.nama_pengajar,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
    }

    return data


@jwt_required
def update(id):
    try:
        inputNamaKelas = request.json['nama_kelas']
        inputNamaPengajar = request.json['nama_pengajar']
        kelas = Kelass.query.filter_by(id=id).first()
        
        kelas.nama_kelas = inputNamaKelas
        kelas.nama_pengajar = inputNamaPengajar
        db.session.commit()
        return response.ok('', 'Successfully update kelas!')
    except Exception as e:
        print(e)

@jwt_required
def show(id):
    try:
        kelas = Kelass.query.filter_by(id=id).first()
        if not kelas:
            return response.badRequest([], 'Empty....')

        data = singleTransform(kelas)
        return response.ok(data, "")
    except Exception as e:
        print(e)

@jwt_required
def delete(id):
    try:
        kelas = Kelass.query.filter_by(id=id).first()
        if not kelas:
            return response.badRequest([], 'Empty....')

        db.session.delete(kelas)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        print(e)


