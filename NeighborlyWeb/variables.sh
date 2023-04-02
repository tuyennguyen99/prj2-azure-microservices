#! /bin/sh
resourceGroup=prj2-udacity
########################################
# Variables for the Function App
# Must be unique worldwide
functionApp=prj2-func02
# Must be unique worldwide
storageAccount=udacityfunca7a3
region=eastasia
########################################
# Variables for MongoDB API resources
# Needs to be lower case
cosmosDBAccountName="prj2admin" 
serverVersion='4.0'
# MongoDB database name
databaseName='azure'
# Collection within the MongoDB database
collectionName='notes'
########################################
# General purpose variables
# uniqueId=$RANDOM
########################################
# Must be unique worldwide
webApp='user187903WebApp'
########################################
containerRegistry='prj2registry'
AKSCluster='prj2cluster'
imageName='prj2image'
imageTag='v1'
########################################
# Print and verify
echo "=======Local Environment Variables======"
echo "functionApp = "$functionApp
echo "resourceGroup = "$resourceGroup
echo "storageAccount = "$storageAccount
echo "region = "$region
echo "cosmosDBAccountName = "$cosmosDBAccountName
echo "serverVersion = "$serverVersion
echo "databaseName = "$databaseName
echo "collectionName = "$collectionName
echo "webApp = "$webApp
echo "containerRegistry = "$containerRegistry
echo "AKSCluster = "$AKSCluster
echo "imageName = "$imageName
echo "imageTag = "$imageTag
echo "=======End of Result======"
echo "docker build -t $imageName:$imageTag"
echo "docker run -p 7071:7071 -it $imageName:$imageTag"
echo "docker tag $imageName:$imageTag $containerRegistry.azurecr.io/$imageName:$imageTag"
echo "docker login $containerRegistry.azurecr.io/"
echo "docker push $containerRegistry.azurecr.io/$imageName:$imageTag"