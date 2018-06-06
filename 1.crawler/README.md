## 前言 ##
首先把爬蟲(crawler)放在第一順位來講解，並不是代表研究的順序，而是整體來看  
爬蟲的部分可以快速帶過，所以把mongodb資料庫寫入的部分就變得沒什麼特殊，但爬蟲調適的耗時也不輸其他項目的。

## 開發工具 ##
<ul>
	<li>語言:Python3.6</li>
	<li>資料庫:mongodb</li>
	<li>資料庫空間:mlab、AWS</li>
	<li>額外插件:datetime、pymongo、requests、json</li>
	<li>爬蟲:Beautifulsoup4(一開始會使用，後來發現api獲得的json不必用到)</li>
	<li>Linux指令:nohup、crontab、kill</li>
</ul>

## 編寫多進程 ##

這邊運用Process來執行多"進"程    
所以有一個主程式py檔來設定到排程上，
用for 迴圈可以執行多個Process,這邊下了11個進程來呼叫py檔
start.py
```python
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import time
def StartSh(path):
    os.system(path)

if __name__ == '__main__':
        
        sh='python crawler01.py '
        li = [sh]

        for i in range(1,11):

            p = Process(target=StartSh, args=(li[0]+str(i),))

            p.start()
```

之前是將腳本丟到AWS上去設定排程跑，不過免費的主機效能很低且多開發現流量會爆表，  
大概摸索了3個月就不在AWS上執行了，因為初衷是以免費為前提練習的，為此花了700多NT。  

## 設定排程 ##

我使用了crontab 來進行排程執行我要的腳本，這邊遇到了很多問題:  
<li>1.運行python start.py 後，關掉終端程序就停了!</li>
解決辦法使用 nohup運行python，就可以在後端運行python。  
<li>2.nohup 運行時，不支援utf-8。</li>
可以寫一個py檔來print(sys.stdout.encoding) ,  
可以在下圖看到用nohup python 執行會出現 None , 一般環境下執行會顯示utf-8 ,  
所以我們要Linux下指令，告訴Linux 環境 nohup 的python 預設需要使用utf-8,  
"export PYTHONIOENCODING=utf-8" ,按下Enter送出後，再次使用nohup 腳本就可以看到顯示utf-8。  

![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/1.crawler/img/nohup.jpg)
<li>3.運行nohup python start.py 後，有些進程不會自己離開，會佔用掉記憶體,最後AWS整個當掉。</li>
因為是免費的AWS所以memory 大小有限，所以crontab 也設定了一個排程用來移除殘存的進程。  
crontab */20 * * * * pkill -9 python，每20分鐘就刪除python所有進程。  

<li>4.crontab 	排程設定如果時間相同時，一個是運行python 一個是pkill python時，會隔次時間才開啟。</li>


## 爬蟲部分 ##
1.圖1是資料庫的部分  
1aws 代表 第一個進程，2aws 代表第二個進程，以此類推。  
字典(dict)裡面的  
start 是每次進程for迴圈裡面的第一個要爬的遊戲編號，  
here 是 當前運行時爬到哪個遊戲編號了，如果中間碰到程序問題還可以記錄還有多少沒爬完。  
edate 是當前爬到的遊戲時間  
end 是這個進程最後結尾的遊戲編號，也就是迴圈最後會到這個遊戲編號後停止。
![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/1.crawler/img/07-1.jpg)  
2. 圖2是爬蟲之前會先去讀取資料庫裡面(1~~11)個進程記錄，把here和end的遊戲編號都抓出來，  
之後透過max(list)的方式查看最新的end最後遊戲編號是多少，這裡查看到是1515871876，下方會藉由這個數字接著繼續爬蟲。  
![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/1.crawler/img/07-2.jpg)
3.圖3 可以看到 將1515871876帶入下方function，這邊設定範圍爬取範圍10，也就是1515871876~1515871886，  
![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/1.crawler/img/cr-1.jpg)  
然後到:  
https://acs-garena.leagueoflegends.com/v1/stats/game/TW/1515871876/timeline  
![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/1.crawler/img/cr-2.jpg)  
https://acs-garena.leagueoflegends.com/v1/stats/game/TW/1515871876  
![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/1.crawler/img/cr-3.jpg)  
可以看到api返回了兩個json，這邊看起來很恐怖對吧~  
