FROM jupyter/minimal-notebook

#RUN conda config --add channels conda-forge

RUN conda create -y -n python2 python=2 ipykernel numpy scipy matplotlib requests obspy

RUN /bin/bash -c " source activate python2 && python -m ipykernel install --user --name python2 --display-name \"Python2\" && exit"

ADD emsc_services.ipynb .
