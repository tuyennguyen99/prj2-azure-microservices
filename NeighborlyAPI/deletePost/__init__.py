import logging
import os
import pymongo
from bson.objectid import ObjectId
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Delete post trigger function processed a request.')
    id = req.params.get('id')

    if id:
        try:
            url = os.environ['CosmosMongoDBConnection']
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['posts']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            logging.error("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
