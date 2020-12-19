import os
import urllib.request
import zipfile
import codecs
import pandas as pd


def load_beauty_rating():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = current_dir + "/beauty_rating/data.csv"
    return pd.read_csv(path)


def load_movielens():
    # MovieLens100kをダウンロードして解凍
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(current_dir + '/ml-100k'):
        urllib.request.urlretrieve('http://files.grouplens.org/datasets/movielens/ml-100k.zip', current_dir + '/ml-100k.zip')
        with zipfile.ZipFile(current_dir + '/ml-100k.zip') as zip_file:
            zip_file.extractall('.')

    # load data
    with codecs.open('ml-100k/u.data', 'r', 'utf-8', errors='ignore') as f:
        data = pd.read_table(f, delimiter='\t', header=None)
        data.rename(
            columns={
                0: 'user_id',
                1: 'item_id',
                2: 'rating',
                3: 'timestamp'
            },
            inplace=True
        )

    with codecs.open('ml-100k/u.item', 'r', 'utf-8', errors='ignore') as f:
        header_text = (
            "movie id | movie title | release date | video release date | IMDb URL | "
            "unknown | Action | Adventure | Animation | Children's | Comedy | Crime | "
            "Documentary | Drama | Fantasy | Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi | "
            "Thriller | War | Western"
        )
        columns = [col.replace('\n', '').replace(' ', '_').lower() for col in header_text.split(' | ')]
        #columns = list(map(lambda f: f.replace('\n', '').replace(' ', '_').lower(), header_text.split(' | ')))
        item = pd.read_table(f, delimiter='|', header=None, names=columns)
        # item.rename(
        #     columns=columns,
        #     inplace=True
        # )

    with codecs.open('ml-100k/u.user', 'r', 'utf-8', errors='ignore') as f:
        user = pd.read_table(f, delimiter='|', header=None)
        user.rename(
            columns={
                0: 'user_id',
                1: 'age',
                2: 'gender',
                3: 'occupation',
                4: 'zip_code'
            },
            inplace=True
        )

    return data, item, user
