sudo docker network create vulnerable --attachable --subnet 10.0.0.0/24;
docker run \
    -it \
    --network vulnerable \
    --ip="10.0.0.3" \
    --name metasploitable \
    --hostname metasploitable2 \
    tleemcjr/metasploitable2 \
    bash;




