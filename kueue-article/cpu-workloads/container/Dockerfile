FROM tensorflow/tensorflow:latest

ENV NUM=10

RUN mkdir -p /code

WORKDIR /code

COPY tensorflow-cpu-test.py ./

ENTRYPOINT python tensorflow-cpu-test.py $NUM