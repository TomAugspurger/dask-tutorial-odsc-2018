# Parallel Data Analysis with Dask

Materials for the [Dask tutorial at ODSC West 2018](https://odsc.com/training/portfolio/cloud-native-data-science-with-dask).

The tutorial is split in two parts. For the first part, we'll use the
environment you created ahead of time on your laptop (see below). Assuming the
WiFi is working, for the second part everyone will use their own Dask Cluster I
set up ahead of time.

If you stumbled across this repository and would like to work through the
materials on your own, consider the official [Dask
Tutorial](https://github.com/dask/dask-tutorial).

## First Time Setup

If you don't have `git` installed, you can download a ZIP copy of the repository using the green button 
("Clone or Download"->"Download ZIP") above.
In this case the file will be called `dask-tutorial-odsc-2018-master`, instead of `dask-tutorial-odsc-2018`.
Adjust the commands below accordingly.

[Install Miniconda](https://conda.io/miniconda.html) or ensure you have Python 3.6 installed on your system.

```
# Update conda
conda update conda

# Clone the repository, or download the ZIP and decompress
git clone https://github.com/martindurant/dask-tutorial-odsc-2018

# Enter the repository
cd dask-tutorial-odsc-2018

# Create the environment
conda env create

# Activate the environment
conda activate dask-scipy

# Download data
python prep_data.py

# Start jupyterlab
jupyter lab

or

jupyter-lab
```

If you aren't using conda

```
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

# Download data
python prep_data.py

# Start jupyterlab
jupyter lab
```

### Installing Graphviz

Graphviz is used by Dask to produce graphical representations graphs in the
notebook. It is an optional extra that you can install.

Although graphviz and it's python bindings are included in the provided
environment, you need extra libraries for it to work on your system, and what
you need depends on your OS

- for linux, you can get graphviz from your
  system package manager, e.g., `apt-get install graphviz`
- for OSX, you can install graphviz with  brew/macports
- for windows, you will need to install from
  https://graphviz.gitlab.io/_pages/Download/Download_windows.html, and set your
  PATH to be able to find the installed executable.

See the [graphviz documentation](https://graphviz.gitlab.io/download/) for further information. 

## Connect to the Cluster

We have a [pangeo](https://github.com/pangeo-data/pangeo) deployment running that'll provide everyone with their own 
cluster to try out Dask on some larger problems.
You can log into the cluster by going to: http://35.226.189.29/
