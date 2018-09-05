![]()

## 前言 ##
學習Django的時候，看到英雄聯盟有各國伺服器的數據戰績網，但是台灣的數據就是沒有人做出來,  
於是抱著學習的心態去製作它，邊做邊學中發現很多東西會運用和經驗就將它記錄下來。  
也看到官網提供的對戰紀錄其實就有api可以查看到json資料，
就在想是不是台服是不是可以直接來爬看看做個數據分析。

## 開發工具 ##
<ul>
	<li>語言:Python3.6</li>
	<li>網頁:Django、javascript、jQuery、HTML、css</li>
	<li>資料庫:mongodb(<a href="https://github.com/kenson2998/python-/tree/master/pymongo%E9%81%8B%E7%94%A8#python-%E9%80%A3%E7%B7%9A-mlab%E8%B3%87%E6%96%99%E5%BA%AB">筆記</a>):  
	<a href="https://github.com/kenson2998/LOL-TW-Rank-analysis/tree/master/1.crawler#%E4%BB%A5%E4%B8%8B%E7%82%BAset%E4%BE%8B%E5%AD%90">$set用法</a>、
	<a href="https://github.com/kenson2998/LOL-TW-Rank-analysis/tree/master/1.crawler#%E4%BB%A5%E4%B8%8B%E7%82%BAinc%E4%BE%8B%E5%AD%90">$inc用法</a>
    </li>
	<li>網路空間:heroku、mlab、AWS、GCP</li>
	<li>前端工具:highchart、echart、bootstrap、nicescroll、semantic、lazyload</li>
	<li>額外插件:timeago(<a href="https://github.com/kenson2998/LOL-TW-Rank-analysis/tree/master/1.crawler#%E9%81%87%E5%88%B0%E6%99%82%E9%96%93%E6%A0%BC%E5%BC%8F%E8%BD%89%E6%8F%9B">時間格式轉換</a>)、telegram-bot</li>
	<li>爬蟲:Beautifulsoup4、Process多進程運用(<a href="https://github.com/kenson2998/LOL-TW-Rank-analysis/tree/master/1.crawler#%E7%B7%A8%E5%AF%AB%E5%A4%9A%E9%80%B2%E7%A8%8B">筆記</a>)、crontab排程運用(<a href="https://github.com/kenson2998/LOL-TW-Rank-analysis/tree/master/1.crawler#%E8%A8%AD%E5%AE%9A%E6%8E%92%E7%A8%8B">筆記</a>)、threading多線程</li>
	
</ul>

## 分析來源 ##
https://acs-garena.leagueoflegends.com/v1/players?name={Id}&region=TW  
https://acs-garena.leagueoflegends.com/v1/stats/game/TW/{uid}  
https://acs-garena.leagueoflegends.com/v1/stats/player_history/TW/{UID}?begIndex=0&endIndex=20&  
https://acs-garena.leagueoflegends.com/v1/stats/game/TW/{gameId}/timeline  

## 遊戲資料來源 ##
https://ddragon.leagueoflegends.com/cdn/{版本}/data/zh_TW/summoner.json  
https://ddragon.leagueoflegends.com/cdn/{版本}/data/zh_TW/item.json  
https://ddragon.leagueoflegends.com/cdn/{版本}/data/zh_TW/champion.json  
https://ddragon.leagueoflegends.com/cdn/{版本}/img/champion/{champname}.png  
https://ddragon.leagueoflegends.com/cdn/{版本}/img/item/{item}.png  
https://ddragon.leagueoflegends.com/cdn/{版本}/img/spell/{Summonerspellname}.png  
https://ddragon.leagueoflegends.com/cdn/{版本}/img/profileicon/{icon}.png  