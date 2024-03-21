# README
2D Rosenbrock example

## Instructions:
1. Build Docker image and name it `umbridge-rosenbrock`:
```
docker build -t umbridge-rosenbrock .
```
and the run the container:
```
docker run -it -p 4243:4243 umbridge-rosenbrock
```

2. Run the emcee client
```
python client.py
```
