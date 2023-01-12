## For Development

- docker-compose build
- docker-compose up

The above will allow you to develop the Go application and every time a save occurs the Go application will be refreshed

## How to build manually (need to rebuild every time update is made)

- docker build -t helloworld -f Dockerfile.prod .
- docker run -it --rm --name prod helloworld
# DockerContainers
