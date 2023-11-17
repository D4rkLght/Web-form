.SILENT:

COLOR_RESET = \033[0m
COLOR_GREEN = \033[32m
COLOR_YELLOW = \033[33m
COLOR_WHITE = \033[00m

.DEFAULT_GOAL := help


.PHONY: help
help:  # Вызвать help
	@echo -e "$(COLOR_GREEN)Makefile help:"
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "$(COLOR_GREEN)-$$(echo $$l | cut -f 1 -d':'):$(COLOR_WHITE)$$(echo $$l | cut -f 2- -d'#')\n"; done


start: # Запуск контейнеров сервиса
	docker-compose -f docker-compose.yaml up -d; \
	if [ $$? -ne 0 ]; \
    then \
        docker compose -f docker-compose.yaml up -d; \
		docker compose version; \
    fi

reload: # Запуск контейнеров сервиса
	docker-compose -f docker-compose.yaml up --build -d; \
	if [ $$? -ne 0 ]; \
    then \
        docker compose -f docker-compose.yaml up --build -d; \
		docker compose version; \
    fi

stop: # Остановка контейнеров сервиса
	docker-compose -f docker-compose.yaml down; \
	if [ $$? -ne 0 ]; \
    then \
		docker compose -f docker-compose.yaml down; \
	fi

clear: # Очистка контейнеров сервиса
	docker-compose -f docker-compose.yaml down --volumes; \
	if [ $$? -ne 0 ]; \
    then \
		docker compose -f docker-compose.yaml down --volumes; \
	fi

load-data:
	docker exec -i web-form_mongodb_1 sh -c 'mongoimport -c forms -d myDatabase --drop' < newdbexport.json
	
server-init: #Базовая команда для запуска сервиса.
	make clear start reload load-data