# GRK Python Workshop

## Installation

### Docker
The easiest way to run the code for the workshop is using a docker image via
```
docker run -it -p 8881:8881  grk2044/base-python:latest bash
```
if you want to make the current folder accessible within the image you need to mount it via `-v $(pwd):<path-to-folder>`

To run a Jupyter Notebook within the Docker image, use the following command:

```
jupyter notebook --ip 0.0.0.0 --no-browser --port 8881
```
### Singularity
Using singularity you can simply run
```
singularity exec --pwd ${PWD} docker://grk2044/base-python:latest jupyter notebook --no-browser --port 8871
```

with the `-B` flag you can mount additional directories

### Virtual Machine

Alternatively you can use a Virtual Machine which can be downloaded [here](http://go.web.cern.ch/go/8Z8J)
