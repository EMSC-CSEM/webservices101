
.PHONY: build run log deamon

build:
	docker build -t jupyter_img .

run:
	docker run --name jupyter_emsc --rm -p 7000:8888 jupyter_img

deamon:
	docker run -d --name jupyter_emsc --rm -p 7000:8888 jupyter_img

log:
	docker logs --follow jupyter_emsc
