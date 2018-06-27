### 說明
因為官方沒有提供計算好的數據api，  

所以只有利用每次戰鬥的數據來收集做大筆大筆的數據分析，  

舉例來說 R社有一個Api可以查看該英雄死亡次數好了，預設它有一組api是直接返回資料庫上統計好的死亡次數。  

但是台服沒有提供這樣的api 那我們要怎麼達到統計死亡數據呢?  

我們唯一能查看到的數據都只有在數以萬計的單筆戰績上去查看，  

透過爬蟲的方式 ，每筆戰鬥資料去撈取死亡數據，計算過後丟到自己的數據庫。  

另外寫多排程來進行計算總合(count)和勝率 (winrate)  

因為每次寫入就計算一次勝率其實有點耗時，所以我們必須在另外跑一組專門計算用的線程，  

參考請看<a href="https://github.com/kenson2998/LOL-TW-Rank-analysis/blob/master/2.analysis/start-do-rate.py">start-do-rate.py</a>和<a href="https://github.com/kenson2998/LOL-TW-Rank-analysis/blob/master/2.analysis/do-rate.py">do-rate.py</a>。  



### 英雄資料勝率分析 ###
運行 start-do-rate.py 運用 Process 多線程開啟更多python 去開do-rate.py  

start-do-rate.py 內容如下:  

```python
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import time
import sys
s=int(sys.argv[1])
sd=int (sys.argv[2])
def StartSh(path):
    os.system(path)

if __name__ == '__main__':
        cd=1
        sh1 = "pkill -9 -f python"

        sh2='python do-rate.py '
        li = [sh2,sh1]
        a=['8.11','8.10','8.12','8.9']
        for i in range(1,15):
            start1=str(i*10-s)
            end1=str(i*10-sd+1)
            p = Process(target=StartSh, args=(sh2+a[2]+' '+start1+' '+end1,))
            p.start()

```
## 多進程 ##

這邊使用multiprocessing 中的 Process 來進行多進程，原因是目前英雄超過140以上，  
再加上每個英雄數據資料有好幾百筆需要計算的話，那需要更多時間。  
![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/2.analysis/img/data-rate1.png)  

利用for 迴圈來把每10個英雄為一個範圍，總共分成14組進程來運算。  
排程的時候分成三組，執行 python start-do-rate.py 10 7,  
10就會帶入s=int(sys.argv[1]),7帶入sd=int (sys.argv[2])  
所以Process最後裡面的值可以解讀為:  
```python
p = Process(target=StartSh, args=('python do-rate.py 8.12 0 4',))
```
```python
p = Process(target=StartSh, args=('python do-rate.py 8.12 140 134',))
```
下一組就是執行 python start-do-rate.py 7 4、python start-do-rate.py 4 0 就可以涵蓋全部英雄資料  

end1 這個變數是每個線程做的範圍。  


## 百分比算法 ##

```python
percentq='{percent:.2%}'.format(percent=round(float(w) / co, 4))
```
因為爬蟲和運算寫入的進程是分開的，所以運算勝率的速度如果不夠快的話，會跟不上爬蟲給的資料。  

例如 spell_list.412的勝率應該是  692/1448 取百分比4位答案應該是 47.49% ,  

這就是勝敗總合值還繼續增加，勝率還沒立即跟上當前資料。  

![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/2.analysis/img/data-rate2.png)

運算完後 使用 $set 回傳資料庫更新場次(count)的值和勝率(winrate)的值，  

```python
collect2.update({'_id': b}, {"$set": {name1: co}})
collect2.update({'_id': b}, {"$set": {name1_1: percentq}})
```

做了幾十萬筆資料後，會發現一個問題，就是有些不具參考的資料存在，  

舉個例子，有一場遊戲中某位玩家贏了或是吵架了，  
在結束遊戲前把裝備全部賣掉或是換成6水滴裝備，這樣就會記錄這英雄一筆6水滴裝備  
有一次剛改版時，因為資料量少，真的有推薦裝備六水滴顯示在網頁上  
所以設定了另一組用來過濾的程式碼，條件是key的長度可能太短的就移除(可能是等級低於15或是裝備少於4件)另一個是場次(co)的值少於3場  

如果達到上述條件就用 $unset 來移除掉該資料。  

```python
if c=='8.6':
    if fname =='skill_list':
        if co < 3 or len(i)<15:# skill_list
            collect2.update({'_id': b},{"$unset": {name2:{}}})
    if fname =='perk_list':
        if co < 3:
            collect2.update({'_id': b},{"$unset": {name2:{}}})
    if fname =='item_top':
        if co < 2 or len(i) < 5:
            collect2.update({'_id': b},{"$unset": {name2:{}}})
            collect2.update({'_id': b}, {"$unset": {name2_1: {}}})
    if fname =='spell_list':
        if co < 3:
            collect2.update({'_id': b},{"$unset": {name2:{}}})
```
start-do-rate.py執行畫面:  
![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/2.analysis/img/start-do-rate.png)  




### 各英雄位置分析 ###

可以參考 <a href="https://github.com/kenson2998/LOL-TW-Rank-analysis/blob/master/2.analysis/do-postion.py">do-postion.py</a>。

![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/2.analysis/img/postion.png)

算完位置後就可以知道路線上有哪些英雄就可以各別算出勝率了  

執行<a href="https://github.com/kenson2998/LOL-TW-Rank-analysis/blob/master/2.analysis/do-rank-rate.py">do-rank-rate.py</a>。

##使用sorted進行勝率排序##

這邊用把最底下全英雄勝率的程式碼來解釋:
```python
data_ps=collect_data.find({})  ### 撈出全部英雄資料
z={}
for xi in data_ps: ### 
    print(xi['_id'])
    if xi['_id']!='bans': #bans表欄位不要運算
        coto=(xi['usetime']['win'])+(xi['usetime']['lose']) #計算該英雄總場次
        z[xi['_id']]=('{percent:.2%}'.format(percent=round(float(xi['usetime']['win'])/coto, 4))),coto #用英雄id當key,value為勝率
print('z:',z) #印出全部英雄勝率
da = sorted(z.items(), key=lambda d: d[1][0], reverse=True) #sorted 進行順序 z的value 為 values的第一個值為勝率，所以用勝率排序 
print('da:',da)
collect_ps.update({'_id': 'winrate'}, {"$set": {'total': da}})
print('done')
```
這邊有一個東西很好用，就是lambda函式  
da = sorted(z.items(), key=lambda d: d[1][0], reverse=True)  
lambda可以解釋成1行for迴圈，所以這邊用法是將全部的d[1][0]來當排序，如果是d[1]就是value，da[1][1]就是使用次數，  
```python
依安妮的資料為例子 
1: ('50.19%', 5280, ['Annie', '安妮', '1'])  
key為:1
value為:('50.19%', 5280, ['Annie', '安妮', '1'])
```
如果寫成da = sorted(z.items(), key=lambda d: d[1][1], reverse=True)   
就是用使用次數做排序  


z是還沒排序前:  
![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/2.analysis/img/z.png)  
da是用sorted函式排序:  
![](https://raw.githubusercontent.com/kenson2998/LOL-TW-Rank-analysis/master/2.analysis/img/da.png)  
