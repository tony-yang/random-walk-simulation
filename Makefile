.DEFAULT_GOAL := start

start:
	docker build -t random-walk .
	docker run -it --rm random-walk python random_walk.py
