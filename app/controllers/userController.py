from app.model.user import Users
from app import response, app
from flask import request
from app import db
from flask_jwt_extended import *

import datetime

@jwt_required
def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)

@jwt_required
def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Empty....')

        data = singleTransform(users, withAbsen=False)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def transform(users):
    array = []
    for i in users:
        array.append(singleTransform(i))
    return array


def singleTransform(users, withAbsen=True):
    data = {
        'id': users.id,
        'nim': users.nim,
        'nama': users.nama,
        'email': users.email,
    }

    if withAbsen:
        absens = []
        for i in users.absens:
            absens.append({
                'id': i.id,
                'created_at': i.created_at,
                'updated_at': i.updated_at,
            })
        data['absens'] = absens

    return data

@jwt_required
def store():
    try:
        nim = request.json['nim']
        nama = request.json['nama']
        email = request.json['email']
        password = request.json['password']

        users = Users(nim=nim, nama=nama, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()
        
        return response.ok('', 'Successfully create data!')


    except Exception as e:
        print(e)

@jwt_required
def update(id):
    try:
        nim = request.json['nim']
        nama = request.json['nama']
        email = request.json['email']
        password = request.json['password']

        user = Users.query.filter_by(id=id).first()
        user.nim = nim
        user.nama = nama
        user.email = email
        user.setPassword(password)

        db.session.commit()

        return response.ok('', 'Successfully update data!')

    except Exception as e:
        print(e)

@jwt_required
def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'Empty....')

        db.session.delete(user)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')

    except Exception as e:
        print(e)

def login():
    try:
        nim = request.json['nim']
        password = request.json['password']

        user = Users.query.filter_by(nim=nim).first()
        if not user:
            return response.badRequest([], 'Empty....')
        
        if not user.checkPassword(password):
            return response.badRequest([], 'Your credentials is invalid')

        data = singleTransform(user,withAbsen=False)
        expires = datetime.timedelta(days=1)
        expires_refresh =datetime.timedelta(days=3)
        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token =create_refresh_token(data, expires_delta=expires_refresh)

        return response.ok({
            "data":data,
            "token_access": access_token,
            "token_refresh": refresh_token,
        },"")

    except Exception as e:
        print(e)

@jwt_refresh_token_required
def refresh():
    try:
        user = get_jwt_identity()
        new_token = create_access_token(identity=user, fresh=False)

        return response.ok({
            "token_access": new_token
        }, "")
    except Exception as e:
        print(e)