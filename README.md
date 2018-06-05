## 前言 ##
學習Django的時候，看到英雄聯盟有各國伺服器的數據戰績網，但是台灣的數據就是沒有人做出來，<br/>
於是抱著學習的心態去製作它，邊做邊學中發現很多東西會運用和經驗就將它記錄下來。  

## 開發工具 ##
<ul>
	<li>語言:Python3.6</li>
	<li>網頁:Django、javascript、jQuery、HTML、css</li>
	<li>資料庫:mongodb</li>
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