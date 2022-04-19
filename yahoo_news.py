import numpy as np
import matplotlib.pyplot as plt

class y_news_class():
    def y_news(self, url):
        import urllib.request, urllib.error
        from bs4 import BeautifulSoup
        import csv

        self.url = url
        # url = "https://kabuoji3.com/stock/6501/2019/"
        # URLを指定する
        html = urllib.request.urlopen(url)
        # URLを開く
        soup = BeautifulSoup(html, "html.parser")
        # BeautifulSoup で開く
        # HTMLからニュース一覧に使用しているaタグを絞りこんでいく
        aaa = soup.select(".newsFeed")
        news_tag = soup.select(".newsFeed_item_title") ###
        # news_tag_2 = soup.select(".newsFeed_item")
        # print (news_tag)

        for i in range(len(news_tag)):
            news_tag[i] = str(news_tag[i]).replace("<div class=\"newsFeed_item_title\">", "").replace("</div>", "")
        return news_tag



if __name__ == '__main__':
    print("ENTER [x] or [X]")
    z = input()

    if (z == "x" or z == "X"):
        news_num = 21        ### yahoo の記事が22 番目まである
        key_words = ["自民"]    ### キーワード(複数可)
        hits = []
        news_books = [[] for j in range(news_num)]
        # theme = ["top-picks", "domestic", "world", "business", "entertainment", "sports", "it", "science", "local"]
        theme = ["top-picks"]


        for l in range(len(theme)):

            for k in range(1, news_num+1):
                # print(theme[l])
                url_url = "https://news.yahoo.co.jp/topics/" + theme[l] + "?page=" + str(k)   ### 最後尾はページ番号
                yyy = y_news_class()
                y_news_data = yyy.y_news(url_url)

                news_books[k-1] = y_news_data
                # print(news_books[k-1])
                # for i in range(len(y_news_data)):
                    # print(y_news_data[i])



            for n in range(len(key_words)):
                for h in range(len(news_books)):
                    for g in range(len(news_books[h])):
                        ccc = news_books[h][g]
                        # print(news_books[h][g])
                        ddd = ccc.find(key_words[n])
                        if (ddd > -1) :
                            # print(ccc[ddd])
                            hits.append(ccc)

        for t in range(len(hits)):
            print(hits[t])
