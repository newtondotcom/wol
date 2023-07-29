IMAGE_NAME=wol
HUB_NAME=newtondotcom/wol:latest
docker build . -f Dockerfile -t $IMAGE_NAME
docker tag $IMAGE_NAME $HUB_NAME
docker push $HUB_NAME