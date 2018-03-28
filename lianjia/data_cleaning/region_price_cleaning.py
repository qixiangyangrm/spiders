import json
import re

with open ('house.LianJiaFangJiaInfo.json','r',encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    # print(line)
    row_data = json.loads(line)
    region_name = row_data['districtThrName']
    duration = eval(row_data['month'])
    districtThrName = row_data['districtThrName']
    referencePrice4 = eval(row_data['referencePrice4'])
    # print(referencePrice4)

    # for price in referencePrice4:
    #     print(price)

    # print(region_name,duration,len(duration))
    month_list = []

    for month in duration:
        month_num = re.compile('\d+').findall(month)[0]
        month_list.append(month_num)

    month_lenth = len (month_list)

    if month_lenth ==12:
        pass
        # print('正常')
        # print(duration)
        #
        # for index,val in enumerate(month_list):
        #     if index <= 9:
        #         if int(val) <=12:
        #             time = '2017-'+ str(val) + '-01'
        #             print(time)
        #     else:
        #         time = '2018-' + str(val) + '-01'
        #         print(time)
    else:
        if month_lenth >2 :
            # pass
            print(month_list)
        else:
            pass
            # print(month_list)
            # print(duration,len(duration))
            # print(index,val)

        # for m in range(0,len(date_list)):
        #     community_name = districtThrName
        #     trend_time = date_list[m]
        #     referencePrice= referencePrice4[m]
        #     print(community_name,trend_time,referencePrice)
    #
    # # else:
    # #     for month in duration:
    # #         month_num = re.compile('\d+').findall(month)[0]
    # #         if int(month_num) <= 10:
    # #             time ='2017-'+ str(month_num)+'-01'
    # #             print(region_name,time)
    # #         else:
    # #             time ='2018-'+ str(month_num)+'-01'
    # #             print(region_name,time)
    # #     # print(districtThrName,region_name,duration)