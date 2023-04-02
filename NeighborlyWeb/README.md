docker login $containerRegistry.azurecr.io
func init --docker-only --python

docker tag flaskappimage $containerRegistry.azurecr.io/flaskappimage
docker push $containerRegistry.azurecr.io/flaskappimage