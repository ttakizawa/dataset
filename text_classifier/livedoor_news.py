import os
import urllib.request
import tarfile
import glob
import gzip
import codecs
import pandas as pd


current_dir = os.path.dirname(os.path.abspath(__file__))

genres = [
    'topic-news',
    'sports-watch',
    'smax',
    'peachy',
    'movie-enter',
    'livedoor-homme',
    'kaden-channel',
    'it-life-hack',
    'dokujo-tsushin'
]


def _download_zip():
    urllib.request.urlretrieve(
        'https://www.rondhuit.com/download/ldcc-20140209.tar.gz',
        current_dir + '/ldcc-20140209.tar.gz'
    )
    tar = tarfile.open(current_dir + '/ldcc-20140209.tar.gz')
    tar.extractall(current_dir)
    tar.close()

def load_news_corpus():

    if os.path.exists(current_dir + '/livedoor_news_corpus.csv'):
        df = pd.read_csv(current_dir + '/livedoor_news_corpus.csv')
        return df

    if not os.path.exists(current_dir + '/text'):
        _download_zip()

    genre_array = []
    urls = []
    dates = []
    titles  = []
    texts = []
    for g in genres:
        files = glob.glob(current_dir + f"/text/{g}/*.txt")
        for file in files:
            if file.split('/')[-1] != 'LICENSE.txt':
                with open(file, 'r') as f:
                    lines=f.readlines()
                    url, date, title, text = lines[0], lines[1], lines[2], '\n'.join(lines[3:])
                    genre_array.append(g)
                    urls.append(url)
                    dates.append(date)
                    titles.append(title)
                    texts.append(text)

    df = pd.DataFrame({
        'genre': genre_array,
        'url':urls,
        'date': dates,
        'title': titles,
        'text': texts
    })
    df.to_csv(current_dir + '/livedoor_news_corpus.csv', index=False)
    return df
