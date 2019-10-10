# GRK Python Workshop

## Installation

The easiest way to run the code for the workshop is using a docker image via
```
docker run -it -p 8881:8881  gitlab-registry.cern.ch/fsauerbu/grk-python-workshop/base-python:latest bash
```
if you want to make the current folder accessible within the image you need to mount it via `-v $(pwd):<path-to-folder>`

To run a Jupyter Notebook within the Docker image, use the following command:

```
jupyter notebook --ip 0.0.0.0 --no-browser --port 8881
```
!TODO Add singularity command
