#-*-coding:utf-8-*-
#嵌套词典
import math
Numberlist={
'白雪萍':{'学号':'1417140301','性别':'女','年龄':18,'成绩信息':80},
'董良':{'学号':'1417140302','性别':'女','年龄':18,'成绩信息':86},
'范佳琪':{'学号':'1417140303','性别':'女','年龄':18,'成绩信息':87},
'郭全威':{'学号':'1417140304','性别':'男','年龄':19,'成绩信息':88},
'金诗琪':{'学号':'1417140305','性别':'女','年龄':18,'成绩信息':92},
'李建':{'学号':'1417140306','性别':'男','年龄':20,'成绩信息':86},
'李奇星':{'学号':'1417140307','性别':'男','年龄':22,'成绩信息':14},
'李思婳':{'学号':'1417140308','性别':'女','年龄':18,'成绩信息':76},
'李易伦':{'学号':'1417140309','性别':'男','年龄':19,'成绩信息':76},
'李哲':{'学号':'1417140310','性别':'女','年龄':18,'成绩信息':88},
'林江':{'学号':'1417140311','性别':'男','年龄':19,'成绩信息':76},
'刘世儀':{'学号':'1417140312','性别':'男','年龄':19,'成绩信息':96},
'刘新':{'学号':'1417140313','性别':'女','年龄':18,'成绩信息':78},
'马艳霞':{'学号':'1417140314','性别':'女','年龄':18,'成绩信息':70},
'缪冬花':{'学号':'1417140315','性别':'女','年龄':18,'成绩信息':69},
'曲友光':{'学号':'1417140316','性别':'男','年龄':19,'成绩信息':77},
'汪进':{'学号':'1417140317','性别':'男','年龄':19,'成绩信息':72},
'王海漫':{'学号':'1417140318','性别':'女','年龄':18,'成绩信息':76},
'王野':{'学号':'1417140319','性别':'女','年龄':18,'成绩信息':77},
'杨朔':{'学号':'1417140320','性别':'女','年龄':18,'成绩信息':70},
'张程':{'学号':'1417140321','性别':'女','年龄':18,'成绩信息':98},
'张硕':{'学号':'1417140322','性别':'男','年龄':19,'成绩信息':77},
'张天翼':{'学号':'1417140323','性别':'女','年龄':20,'成绩信息':89},
'张肖':{'学号':'1417140324','性别':'男','年龄':21,'成绩信息':90},
'张泽正':{'学号':'1417140325','性别':'女','年龄':18,'成绩信息':80},
'章华':{'学号':'1417140326','性别':'女','年龄':18,'成绩信息':86}
}



#Print all the student name, student number, gender, age, grade information

print 'Print all the student name:'
for name in Numberlist.keys():
    print name

print 'Print all the student name, student number, gender, age, grade information'
for name in Numberlist.keys():
    print 'name:' , name , '学号:' , Numberlist[name]['学号'] , '性别:' , Numberlist[name]['性别'] , '年龄:', Numberlist[name]['年龄'] , '成绩信息:'  , Numberlist[name]['成绩信息']

    
    
    
    

#增加学生输入
#Numberlist['name']={'学号':'xxxxxx','性别':'xx','年龄':xx,'成绩信息':xx}


#删除学生输入   
#del  Numberlist['name']  
#name属于 Numberlist里的名字 
  
#修改信息输入    
#Numberlist['name']['所要修改的信息'] = '所修改的数据'
       
#查找信息输入    
#Numberlist['name']['所要查找的信息']  

names=['白雪萍','董良','范佳琪',
'郭全威','金诗琪','李建',
'李奇星','李思婳','李易伦',
'李哲','林江','刘世儀',
'刘新','林江','刘世儀',
'刘新','马艳霞','缪冬花',
'曲友光','汪进','王海漫'
'王野','杨朔','张程',
'张硕','张天翼','张肖',
'张泽正','章华']

grades=[80,86,87,
88,92,86,
14,76,76,
88,76,96,
78,70,69,
77,72,76,
77,70,98,
77,89,90,
80,86]









ages=[18,18,18,
18,18,20,
22,18,19,
18,19,19,
18,18,18,
19,19,18,
18,89,18,
19,20,21,
18,18]







import math
print '---------------------------------------------------------------------'
print '全班人数',len(names)                                 #全班人数
print '---------------------------------------------------------------------'
print '最大年龄',max(ages)                                  #最大年龄
print '---------------------------------------------------------------------'
print '最小年龄',min(ages)                                  #最小年龄
print '---------------------------------------------------------------------'
print '平均年龄',(1.0*sum(ages)/len(ages))                  #平均年龄
print '---------------------------------------------------------------------'
print '最高成绩',max(grades)                                #最高成绩
print '---------------------------------------------------------------------'
print '最低成绩',min(grades)                                #最低成绩
print '---------------------------------------------------------------------'
print '平均成绩',1.0*sum(grades)/len(grades)               #平均成绩










