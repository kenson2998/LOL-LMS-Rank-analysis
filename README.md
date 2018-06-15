## 前言 ##
學習Django的時候，看到英雄聯盟有各國伺服器的數據戰績網，但是台灣的數據就是沒有人做出來,  
於是抱著學習的心態去製作它，邊做邊學中發現很多東西會運用和經驗就將它記錄下來。  
也看到官網提供的對戰紀錄其實就有api可以查看到json資料，
就在想是不是台服是不是可以直接來爬看看做個數據分析。

## 開發工具 ##
<ul>
	<li>語言:Python3.6</li>
	<li>網頁:Django、javascript、jQuery、HTML、css</li>
	<li>資料庫:<a url="https://github.com/kenson2998/LOL-TW-Rank-analysis/tree/master/1.crawler#%E4%BB%A5%E4%B8%8B%E7%82%BAset%E4%BE%8B%E5%AD%90">mongodb</a></li>
	<li>網路空間:heroku、mlab、AWS、GCP</li>
	<li>前端工具:highchart、echart、bootstrap、nicescroll、semantic、lazyload</li>
	<li>額外插件:timeago、telegram-bot</li>
	<li>爬蟲:Beautifulsoup4、Process多進程運用、crontab排程運用、threading多線程</li>
	
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