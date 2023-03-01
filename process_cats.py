import time
from pathlib import Path
import multiprocessing
import requests

URL = 'https://cataas.com/cat'
CATS_WE_WANT = 10
OUT_PATH = Path(__file__).parent / 'cats'
OUT_PATH.mkdir(exist_ok=True, parents=True)
OUT_PATH = OUT_PATH.absolute()


def get_cat(url: str, id: str):
    file_path = "{}/{}.png".format(OUT_PATH, id)
    response = requests.get(url, timeout=(5, 5))
    print(response.status_code)
    if response.status_code != 200:
        return
    with open(file_path, 'wb') as ouf:
        ouf.write(response.content)


def load_images_multiprocessing():
    procs = []
    for i in range(CATS_WE_WANT):
        proc = multiprocessing.Process(
            target=get_cat,
            args=(URL, i),
        )
        proc.start()
        procs.append(proc)

    for proc in procs:
        proc.join()

    print(len(procs))


def main():
    load_images_multiprocessing()


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
