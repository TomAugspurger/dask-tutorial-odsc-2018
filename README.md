# Parallel Data Analysis with Dask

Materials for the [Dask tutorial at SciPy 2018](https://scipy2018.scipy.org/ehome/index.php?eventid=299527&tabid=711308&cid=2229599&sessionid=21547348&sessionchoice=1&).

Note that if you are attending the tutorial in person, a cluster will be available should your local
installation fail. We will be all using the shared cloud resources for the later distributed part of the
tutorial.


## First Time Setup

If you don't have `git` installed, you can download a ZIP copy of the repository using the green button 
("Clone or Download"->"Download ZIP") above.
In this case the file will be called `dask-tutorial-scipy-2018-master`, instead of `dask-tutorial-scipy-2018`.
Adjust the commands below accordingly.


[Install Miniconda](https://conda.io/miniconda.html) or ensure you have Python 3.6 installed on your system.

```
# Update conda
conda update conda

# Clone the repository, or download the ZIP and decompress
git clone https://github.com/martindurant/dask-tutorial-scipy-2018

# Enter the repository
cd dask-tutorial-scipy-2018

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
git clone https://github.com/martindurant/dask-tutorial-scipy-2018

# Enter the repository
cd dask-tutorial-scipy-2018

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

Graphviz is used by Dask to produce graphical representations graphs in the notebook. It is an optional extra that
you can install.

Although graphviz and it's python bindings are included in the provided environment, you need extra libraries for it
to work on your system, and what you need depends on your OS

- for linux, you can get graphviz from your
system package manager, e.g., `apt-get install graphviz`
- for OSX, you can install graphviz with 
brew/macports
- for windows, you will need to install from https://graphviz.gitlab.io/_pages/Download/Download_windows.html ,and
set your PATH to be able to find the installed executable.

See the [graphviz documentation](https://graphviz.gitlab.io/download/) for further information. 

## Connect to the Cluster

We have a [pangeo](https://github.com/pangeo-data/pangeo) deployment running that'll provide everyone with their own 
cluster to try out Dask on some larger problems.
You can log into the cluster by going to: http://35.226.189.29/
