FROM tensorflow/tensorflow:2.20.0rc0-gpu

ENV NUM=10

RUN mkdir -p /code

WORKDIR /code

COPY tensorflow-gpu-test.py ./

RUN pip install --extra-index-url https://pypi.nvidia.com tensorflow[and-cuda]

ENTRYPOINT python tensorflow-gpu-test.py $NUM