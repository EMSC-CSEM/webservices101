
.PHONY: build run

build:
	docker build -t jupyter_img

run:
	docker run --name jupyter_emsc -d --rm -p 7000:8888 jupy_img

copy:
	cp /opt/jupyter-anaconda/notebooks/landes/epos/emsc_services.ipynb .

