#算出每個英雄的使用路線和統計暫比，超過37%使用率，此英雄就會加入該位置。
# -*- coding: utf-8 -*-
import pymongo
import sys
fcz='8.12'
urib = "mongodb://user:user@ds000000.mlab.com:000000/gamedata01-1"
clientb = pymongo.MongoClient(urib)
dbb = clientb['gamedata01-1']
collect2b = dbb[fcz]
data=collect2b.find() #這邊如果用find_one()，使用for讀取會有問題，故用find()
pst=['TOP','DUO_SUPPORT','JUNGLE','MIDDLE','DUO_CARRY']
top_list,jg_list,mid_list,ad_list,sup_list =[],[],[],[],[]
for ii in data:
    print(ii['_id'])
    if ii['_id']!='bans': #bans資料欄位撇除，其他就是英雄的資料
        #print('英雄:',ii['_id'])
        data1=collect2b.find_one({'_id':int(ii['_id'])})
        ds = data1['usetime']
        h=ds['win']+ds['lose']  #勝敗加總，算出總場次
        for npst in pst: #pst 列表中的各個位置帶入data1
            try:
                ds = data1[npst]
                cohow=0
                for iia in ds: #假如是top位置，有各個排位的場次
                    try:
                        cohow=cohow+ds[iia]['count']
                    except:
                        pass
                if  round(float(cohow)/h, 4) >0.37: #如果總場次超過37%代表，在那個線路經常使用
#                     print(ii,npst,('{percent:.2}'.format(percent=round(cohow/h, 4))))
                    if npst=='TOP':
                        top_list.append(ii['_id'])
                    if npst=='JUNGLE':
                        jg_list.append(ii['_id'])
                    if npst=='MIDDLE':
                        mid_list.append(ii['_id'])
                    if npst=='DUO_CARRY':
                        ad_list.append(ii['_id'])
                    if npst=='DUO_SUPPORT':
                        sup_list.append(ii['_id'])
            except:
                print('no:',npst) #如果該英雄從來沒有在TOP有資料，就例外印出no,繼續到下一個位置去統計
#以下印出統計完的各位置列表，就是各頁面上呈現的英雄列表了。
print('top:',top_list)
print('jg:',jg_list)
print('mid:',mid_list)
print('ad:',ad_list)
print('sup:',sup_list)
collect_ch = dbb['champion_s']
fff = collect_ch.find_one({'_id': 'ps'})
collect_ch.update(fff, {"$set": {'top': top_list,'jg':jg_list,'mid':mid_list,'ad':ad_list,'sup':sup_list}})
