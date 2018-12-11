from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            message = "A store with name {} already exists.".format(name)
            return {"message": message}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            message = "A error ocurred while creating store."
            return {"message": message}, 500
        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return store.json(), 201


class StoreList(Resource):

    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
