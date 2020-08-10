# What's this?
Collect co2 metrix by mh_z19 sensor and send it to TreasureData using Fluent-Bit

# how to setup
## Build docker image
```
docker build -t waysaku/mh_z19_fluent-bit .
```

## Run docker container
docker run --device=/dev/ttyS0:/dev/ttyS0 -d -ti waysaku/mh_z19_fluent-bit

## check logs
docker logs -f --tail="10" 94eb2b81ad53
