# Build your Docker image
docker build -t timer-api .

# Run your Docker container
docker run -it --rm -p 5000:5000 timer-api

