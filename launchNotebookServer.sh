#!/bin/bash
docker run -it -v "${PWD}/code":"/home/jovyan" -p 8888:8888 algo2-jupyter-image
