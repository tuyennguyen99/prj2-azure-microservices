import logging
import os
import azure.functions as func
import pymongo
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Create post HTTP trigger function processed a request.')
    request = req.get_json()
    if id:
        try:
            url = os.environ['CosmosMongoDBConnection']
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['posts']
            rec_id1 = collection.insert_one(request)
            return func.HttpResponse(req.get_body())
        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)
    return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400)
