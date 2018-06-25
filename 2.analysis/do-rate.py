# -*- coding: utf-8 -*-
import pymongo
import sys
def fu(a,b,c):

    urib = "mongodb://user:user@ds000000.mlab.com:000000/gamedata01-1"
    clientb = pymongo.MongoClient(urib)
    db = clientb['gamedata01-1']
    collect2 = db[c]
    # print(b)
    loga = collect2.find_one({'_id': b})
    fname=a
    for i in loga[fname]:
        if i!='':
            print(c,':',b,':',a,':',i)
            w,l,co=0,0,0
            try:
                l = loga[fname][i]['lose']
            except:
                w = loga[fname][i]['win']
            try:
                w = loga[fname][i]['win']
            except:
                l = loga[fname][i]['lose']
            co=w+l
            try:
                percentq='{percent:.2%}'.format(percent=round(float(w) / co, 4))
            except:
                percentq='0.0%'
            name1=fname+"."+str(i)+'.count'
            name1_1 = fname + "." + str(i) + '.winrate'
            name2 =fname+"."+str(i)
            name2_1 = 'item_list.' + str(i)
            collect2.update({'_id': b}, {"$set": {name1: co}})
            collect2.update({'_id': b}, {"$set": {name1_1: percentq}})
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
        else :
            print('i=""',i)
    # log0 = collect2.find_one({'_id': b})
    # ds=log0[fname]
    # da = sorted(ds.items(), key=lambda d: d[1]['winrate'] , reverse=True)#排序大到小
    # da1 = sorted(ds.items(), key=lambda d: d[1]['count'] , reverse=True)#排序>大到小
    # try:
    #     print(fname,'高勝率:',da[0],da[1],'高選率:',da1[0],da1[1])
    # except:
    #     print(fname,da,da1)
    print(b,':done')
fcz=sys.argv[1]
star=int(sys.argv[2])
en=int(sys.argv[3])
urib = "mongodb://user:user@ds000000.mlab.com:000000/gamedata01-1"
clientb = pymongo.MongoClient(urib)
dbb = clientb['gamedata01-1']
collect2b = dbb[fcz]
#data=collect2b.find_one({})
#llis=[]
#for kk in data:
    #llis.append(kk)
data=collect2b.find({})
llis=[]
for kk in data:
    llis.append(kk['_id'])

for kk in range(star,en):
    try:
        gg=str(llis[kk])
        print('gg:',gg)
        if gg == '_id' or gg== 'version':
            pass
        else:

            keyman=int(llis[kk])
            log0 = collect2b.find_one({'_id': keyman})
            for a in log0:
                if a=='_id' or a=='NONE' or a=='usetime' or a=='game_static' or a=='version' or a=='item_list' :
                    pass
                else:
                    fu(a, keyman,fcz)
    except:
        print('er:',llis,kk)
