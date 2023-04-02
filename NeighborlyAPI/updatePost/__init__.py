import azure.functions as func
import logging
import os
import pymongo
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()
    if request:
        try:
            url = os.environ['CosmosMongoDBConnection']
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['posts']
            
            filter_query = {'_id': ObjectId(id)}

            update_query = {"$set": request}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            logging.error("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

