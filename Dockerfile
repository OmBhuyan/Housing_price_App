FROM continuumio/miniconda3 AS builder

COPY environment.yml .

RUN conda env create -f environment.yml

RUN conda install -c conda-forge conda-pack

RUN conda-pack -n env1 -o /tmp/env.tar && \
    mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
    rm /tmp/env.tar

RUN /venv/bin/conda-unpack


FROM python:3.8-slim-buster

COPY --from=builder /venv /venv

COPY . /housing_price_flaskapp
WORKDIR /housing_price_flaskapp
SHELL ["/bin/bash", "-c"]

EXPOSE 5000

ENTRYPOINT source /venv/bin/activate && \
    gunicorn --bind 0.0.0.0:5000 --log-file logs/log.log --log-level DEBUG app:app