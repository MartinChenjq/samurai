from flask import Blueprint, request, abort
from samurai import app, db, mongo
from samurai.models import User
from samurai.serializers import users_serializer, user_serializer
from samurai.validators import user_schema
from uuid import uuid4
import redis

user_bp = Blueprint('user', __name__)

pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
redis_store = redis.Redis(connection_pool=pool)

@app.route('/users')
def read_users():
    users = db.session.query(User).all()
    return {'data': users_serializer.dump(users)}


@app.route('/users/<int:id>')
def read_user(_id):
    user = db.session.query(User).filter(User.id == _id).first()
    return {'data': user_serializer.dump(user)}


@app.route('/users/mongo')
def read_user_in_mongo():
    if not user_schema.validate(request.args):
        abort(400)
    name = request.args.get('name')
    online_users = mongo.db.Employee.find_one({"name": name})
    if not online_users:
        abort(404)
    online_users.pop('_id')
    return online_users

@app.route('/ping')
def ping():
    uuid = uuid4().hex

    redis_store.set('uuid', uuid)
    _uuid = redis_store.get('uuid')
    return {"uuid4":uuid}


