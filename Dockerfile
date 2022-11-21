FROM node:16.15.0 AS builder
ADD ./frontend/package.json /frontend/package.json
WORKDIR /frontend
RUN yarn install
ADD ./frontend /frontend
RUN yarn build --base="/routes/anonymization/web/"

FROM python:3.7-slim
EXPOSE 8080
RUN pip install "spacy<3.3.0" && pip install https://huggingface.co/bullmount/it_nerIta_trf/resolve/main/it_nerIta_trf-any-py3-none-any.whl
ADD ./requirements.txt /
RUN pip install -r /requirements.txt
COPY --from=builder /frontend/dist /frontend/dist
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ADD . /plugin
ENV PYTHONPATH=$PYTHONPATH:/plugin
WORKDIR /plugin/services
CMD python services.py