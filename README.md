# Parallel Data Analysis with Dask

Materials for the [Dask tutorial at ODSC West 2018](https://odsc.com/training/portfolio/cloud-native-data-science-with-dask).

The tutorial is split in two parts. For the first part, we'll use the
environment you created ahead of time on your laptop (see below). Assuming the
WiFi is working, for the second part everyone will use their own Dask Cluster we
set up ahead of time.

If you are actively in the tutorial and ready to use your cluster, press this
button:

<a href="http://binder.pangeo.io/v2/gh/TomAugspurger/dask-tutorial-odsc-2018/master">
  <img src="http://binder.pangeo.io/badge.svg"
       width="500px">
</a>

If you stumbled across this repository and would like to work through the
materials on your own, consider the official [Dask
Tutorial](https://github.com/dask/dask-tutorial).

## First Time Setup

If you don't have `git` installed, you can download a ZIP copy of the repository using the green button
("Clone or Download"->"Download ZIP") above.
In this case the file will be called `dask-tutorial-odsc-2018-master`, instead of `dask-tutorial-odsc-2018`.
Adjust the commands below accordingly.

[Install Miniconda](https://conda.io/miniconda.html) or ensure you have Python 3.6+ installed on your system.

```bash
# Update conda
conda update conda

# Clone the repository, or download the ZIP and decompress
git clone https://github.com/martindurant/dask-tutorial-odsc-2018

# Enter the repository
cd dask-tutorial-odsc-2018

# Create the environment
conda env create

# Activate the environment
conda activate dask-odsc

# Install the dask-labextension
jupyter labextension install dask-labextension

# Download data
python prep_data.py

# Start jupyterlab
jupyter lab

or

jupyter-lab
```

Using python / virtualenv instead of conda. Note that you're required to already
have `python3` installed and on your PATH before running this. If you want the
full experience, you should also install [graphviz documentation](https://graphviz.gitlab.io/download/)
and [nodejs](https://nodejs.org/en/), but those are optional. Don't worry if you can't
get them installed.

```bash
# Clone the repository, or download the ZIP and decompress
git clone https://github.com/martindurant/dask-tutorial-odsc-2018

# Enter the repository
cd dask-tutorial-odsc-2018

# Create a virtualenv
python3 -m venv .env

# Activate the env
# See https://docs.python.org/3/library/venv.html#creating-virtual-environments
# For bash it's
source .env/bin/activate

# Install the dependencies
python -m pip install -r requirements.txt

# Install the dask-labextension
# Note: this requires npm to be on your PATH
# just ignore it if this doesn't work
jupyter labextension install dask-labextension

# Download data
python prep_data.py

# Start jupyterlab
jupyter lab
```

## Connect to the Cluster

We have a [pangeo](https://github.com/pangeo-data/pangeo) deployment running that'll provide everyone with their own
cluster to try out Dask on some larger problems.
