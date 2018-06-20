# Parallel Data Analysis with Dask

Materials for the [Dask tutorial at SciPy 2018](https://scipy2018.scipy.org/ehome/index.php?eventid=299527&tabid=711308&cid=2229599&sessionid=21547348&sessionchoice=1&).

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
conda env create -c defaults - c conda-forge

# Activate the environment
conda activate dask-scipy

# Download data
python prep_data.py

# Start jupyterlab
jupyter lab
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

## Connect to the Cluster

We have a [pangeo](https://github.com/pangeo-data/pangeo) deployment running that'll provide everyone with their own 
cluster to try out Dask on some larger problems.
You can log into the cluster by going to: TBD
