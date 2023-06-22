IMAGE_NAME=wol
HUB_NAME=newtondotcom/wol:0.0.2
docker build . -f Dockerfile -t $IMAGE_NAME
docker tag $IMAGE_NAME $HUB_NAME
docker push $HUB_NAME