from pymongo import MongoClient
class DAL:

    def __init__(self,host,user_name,password,db_name,collection):
            my_client = MongoClient(f"mongodb://{user_name}:{password}@{host}:27017/{db_name}?authSource=admin")
            db = my_client[db_name]
            self.collection = db[collection]


    def get(self):
        return list(self.collection.find({},{"_id":False}))


    def post(self,id,first_name,last_name,phone_number,rank):
        pass

    def put(self,id,field,new_data):
        pass

    def delete(self,id):
        pass