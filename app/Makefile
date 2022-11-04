# enviroment variables are

# POETRY COMMANDS

PROJECT_ID=kavi-dummy-project-123

.PHONY: install
pinstall:
	poetry install

.PHONY: build
pbuild: install
	poetry build

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --without-hashes -o requirements.txt

.PHONY: black
black:
	poetry run black .

.PHONY: pytest
pytest:
	poetry run pytest --cov=./tests --black -rAP 

.PHONY:black
black:
	isort


# DOCKER / CONTAINER REGISTRY COMMANDS
CONTAINER_NAME=template
PROJECT_ID=kavi-prod-data-lab-4943

.PHONY: build
build:
	docker build -t gcr.io/$(PROJECT_ID)/$(CONTAINER_NAME) .

.PHONY: run
run: build
	docker run -it --name ${CONTAINER_NAME} gcr.io/$(PROJECT_ID)/$(CONTAINER_NAME)

.PHONY: push
push: build
	docker push gcr.io/$(PROJECT_ID)/$(CONTAINER_NAME)

.PHONY: attach
attach:
	docker exec -it $(CONTAINER_NAME) /bin/bash


# CLOUD SLQ PROXY COMMANDS
proxy_download:
	curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64
	chmod +x cloud_sql_proxy

proxy:
	./cloud_sql_proxy -instances=[project]:us-central1:[db-name]=tcp:5434