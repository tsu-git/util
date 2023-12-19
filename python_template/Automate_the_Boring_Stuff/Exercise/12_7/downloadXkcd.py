#!/usr/bin/python
"""downloadXkcd.py

    XKCDのコミックを1つずつダウンロード
"""
import requests, os, bs4
import time

"""target element sample
    <img src="//imgs.xkcd.com/comics/puzzles.png" title="Why couldn't the amulet have been hidden by Aunt Alice, who understands modern key exchange algorithms?" alt="Puzzles" srcset="//imgs.xkcd.com/comics/puzzles_2x.png 2x" style="image-orientation:none">
"""

WAIT_SEC = 5
url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # ページをダウンロードする
    print(f'ページをダウンロード中 {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # コミック画像のURLを見つける
    comic_elem = soup.select('#comic > img')
    if comic_elem == []:
        print('コミック画像が見つかりませんでした')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        # 画像をダウンロードする
        print(f'画像をダウンロード中 {comic_url}...')
        res = requests.get(comic_url)
        res.raise_for_status()

        # 画像を./xkcdに保存する
        with open(
            os.path.join(
                'xkcd', os.path.basename(comic_url)), 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)

    print(f'サーバー負荷軽減のため、{WAIT_SEC}秒間待機。')
    time.sleep(WAIT_SEC)

    # PrevボタンのURLを取得する
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev_link.get('href')


print('完了')
