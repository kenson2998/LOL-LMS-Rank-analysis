# -*- coding: utf-8 -*-
import pymongo
import sys
fcz='8.12'
urib = "mongodb://user:user@ds000000.mlab.com:000000/gamedata01-1"
clientb = pymongo.MongoClient(urib)
dbb = clientb['gamedata01-1']
collect_data = dbb[fcz]
collect_ps = dbb['champion_s8.12']
data_ps=collect_ps.find_one({'_id':'ps'})

pst=['top','sup','jg','mid','ad']
ranklist=['UNRANKED','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','MASTER','CHALLENGER','total']
for iiii in pst:
    dz={'UNRANKED':{},'BRONZE':{},'SILVER':{},'GOLD':{},'PLATINUM':{},'DIAMOND':{},'MASTER':{},'CHALLENGER':{},'total':{}}
    for iii in data_ps[iiii]:
        ver_data=collect_data.find_one({'_id':iii})
        dz[ranklist[0]][iii]=ver_data['rank_use_list']['UNRANKED']['winrate'],ver_data['rank_use_list']['UNRANKED']['count']
        dz[ranklist[1]][iii]=ver_data['rank_use_list']['BRONZE']['winrate'],ver_data['rank_use_list']['BRONZE']['count']
        dz[ranklist[2]][iii]=ver_data['rank_use_list']['SILVER']['winrate'],ver_data['rank_use_list']['SILVER']['count']
        dz[ranklist[3]][iii]=ver_data['rank_use_list']['GOLD']['winrate'],ver_data['rank_use_list']['GOLD']['count']
        dz[ranklist[4]][iii]=ver_data['rank_use_list']['PLATINUM']['winrate'],ver_data['rank_use_list']['PLATINUM']['count']
        dz[ranklist[5]][iii]=ver_data['rank_use_list']['DIAMOND']['winrate'],ver_data['rank_use_list']['DIAMOND']['count']
        dz[ranklist[6]][iii]=ver_data['rank_use_list']['MASTER']['winrate'],ver_data['rank_use_list']['MASTER']['count']
        dz[ranklist[7]][iii]=ver_data['rank_use_list']['CHALLENGER']['winrate'],ver_data['rank_use_list']['CHALLENGER']['count']
        coto=ver_data['usetime']['win']+ver_data['usetime']['lose']
        dz[ranklist[8]][iii]=('{percent:.2%}'.format(percent=round(float(ver_data['usetime']['win'])/coto, 4))),coto
#     print('dz',dz)
    for zii in range(len(ranklist)):

        da = sorted(dz[ranklist[zii]].items(), key=lambda d: d[1][0], reverse=True)
        d=iiii+'.'+ranklist[zii]
        collect_ps.update({'_id': 'winrate'}, {"$set": {d: da}})

data_ps=collect_data.find({})
z={}
for xi in data_ps:
    print(xi['_id'])
    if xi['_id']!='bans':
        coto=(xi['usetime']['win'])+(xi['usetime']['lose'])
        z[xi['_id']]=('{percent:.2%}'.format(percent=round(float(xi['usetime']['win'])/coto, 4))),coto
print('z:',z)
da = sorted(z.items(), key=lambda d: d[1][0], reverse=True)
print('da:',da)
collect_ps.update({'_id': 'winrate'}, {"$set": {'total': da}})
print('done')

