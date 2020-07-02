FROM            ubuntu:16.04
MAINTAINER      MIT Probabilistic Computing Project

                # Fetch dependencies from apt.
RUN             apt-get update -qq \
                && apt-get install -qq -y \
                    build-essential \
                    cython \
                    git \
                    python-matplotlib \
                    python-numpy \
                    python-pandas \
                    python-pytest \
                    python-scipy \
                    python-six \
                    python-sklearn \
                    python-statsmodels \
                    python-virtualenv

                # Create a virtualenv with jupyter.
RUN             virtualenv --system-site-packages /venv
RUN             . /venv/bin/activate && pip install jupyter-core==4.6.1
RUN             . /venv/bin/activate && pip install bokeh
RUN             . /venv/bin/activate && pip install --upgrade 'setuptools<45.0.0'
RUN             . /venv/bin/activate && pip install jupyter
RUN             . /venv/bin/activate && pip install matplotlib --upgrade

                # Clone the probcomp dependencies.
RUN             git clone https://github.com/probcomp/crosscat.git
RUN             git clone https://github.com/probcomp/cgpm.git
RUN             git clone https://github.com/probcomp/trcrpm.git
RUN             git clone https://github.com/nick-torenvliet/bnp_time_series.git

                # Install into the virtualenv.
RUN             . /venv/bin/activate && cd /crosscat && pip install .
RUN             . /venv/bin/activate && cd /cgpm && pip install .
RUN             . /venv/bin/activate && cd /trcrpm && pip install .

                # Run the tests.
RUN             . /venv/bin/activate && python -m pytest --pyargs trcrpm

EXPOSE 		8888
