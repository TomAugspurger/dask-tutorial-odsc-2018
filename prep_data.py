from __future__ import print_function

import os
import argparse
import numpy as np
import pandas as pd
import tarfile
import urllib.request
import zipfile
from glob import glob

data_dir = 'data'


def parse_arguments(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--small", action="store_true", default=False)
    parser.add_argument("--dataset",
                        default="all",
                        choices=['all', 'flights', 'array', 'weather'])
    return parser.parse_args(args)


def flights(small=False):
    flights_raw = os.path.join(data_dir, 'nycflights.tar.gz')
    flightdir = os.path.join(data_dir, 'nycflights')
    jsondir = os.path.join(data_dir, 'flightjson')

    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    if not os.path.exists(flights_raw):
        print("- Downloading NYC Flights dataset... ", end='', flush=True)
        url = "https://storage.googleapis.com/dask-tutorial-data/nycflights.tar.gz"
        urllib.request.urlretrieve(url, flights_raw)
        print("done", flush=True)

    if not os.path.exists(flightdir):
        print("- Extracting flight data... ", end='', flush=True)
        tar_path = os.path.join('data', 'nycflights.tar.gz')
        with tarfile.open(tar_path, mode='r:gz') as flights:
            flights.extractall('data/')
        print("done", flush=True)

    if not os.path.exists(jsondir):
        print("- Creating json data... ", end='', flush=True)
        os.mkdir(jsondir)
        for path in glob(os.path.join('data', 'nycflights', '*.csv')):
            prefix = os.path.splitext(os.path.basename(path))[0]
            # Just take the first 10000 rows for the demo
            df = pd.read_csv(path).iloc[:10000]
            df.to_json(os.path.join('data', 'flightjson', prefix + '.json'),
                       orient='records', lines=True)
        print("done", flush=True)

    print("** Finished! **")


def random_array(small=False):
    if os.path.exists(os.path.join('data', 'random.hdf5')):
        return

    print("Create random data for array exercise")
    import h5py

    if small:
        stop = 100000
        step = 1000
    else:
        stop = 1000000000
        step = 1000000

    with h5py.File(os.path.join('data', 'random.hdf5')) as f:
        dset = f.create_dataset('/x', shape=(stop,), dtype='f4')
        for i in range(0, stop, step):
            dset[i: i + step] = np.random.exponential(size=step)


def weather(small=False):
    if small:
        growth = 400
    else:
        growth = 1200

    url = 'https://storage.googleapis.com/dask-tutorial-data/weather-small.zip'
    weather_zip = os.path.join('data', 'weather-small.zip')
    weather_small = os.path.join('data', 'weather-small')

    if not os.path.exists(weather_zip):
        print("Downloading weather data.")
        urllib.request.urlretrieve(url, weather_zip)

    if not os.path.exists(weather_small):
        print("Extracting to {}".format(weather_small))
        zf = zipfile.ZipFile(weather_zip)
        zf.extractall(data_dir)

    filenames = sorted(glob(os.path.join('data', 'weather-small', '*.hdf5')))

    if not os.path.exists(os.path.join('data', 'weather-big')):
        os.mkdir(os.path.join('data', 'weather-big'))

    if all(os.path.exists(fn.replace('small', 'big')) for fn in filenames):
        return

    from skimage.transform import resize
    import h5py

    for fn in filenames:
        with h5py.File(fn, mode='r') as f:
            x = f['/t2m'][:]

        new_shape = tuple(s * growth // 100 for s in x.shape)

        y = resize(x, new_shape, mode='constant')

        out_fn = os.path.join('data', 'weather-big', os.path.split(fn)[-1])

        try:
            with h5py.File(out_fn) as f:
                f.create_dataset('/t2m', data=y, chunks=(500, 500))
        except Exception as e:
            print(e)
            pass


def main(args=None):
    args = parse_arguments()

    print("Setting up data directory")
    print("-------------------------")

    if args.dataset in ("flights", "all"):
        flights(args.small)
    elif args.dataset in ("array", "all"):
        random_array(args.small)
    else:
        weather(args.small)

    print('Finished!')


if __name__ == '__main__':
    main()
