import json  # since JSON file is large, hence making use of json

# f = open ('dit.json')
# content = json.items(f, 'item') # json loads quickly here as compared to when json.load(f) is used.
# print(set(i['score'] for i in content)) #this line is actually taking a long time to get processed.


# with open('dit.json', 'r') as j:
#     json_data = json.load(j)
    # print(json_data)
    # print(json_data['ssn_variations'])

    # size=len(json_data['ssn_variations'])
    # uniqueNames = []
    # t={}
    # for i,j in json_data['ssn_variations'].items():
    #     # print(i,j)
    #     if j not in uniqueNames:
    #         t[i]=j
    #         # print(t)
    #         uniqueNames.append(j)

    # print('-----------------')
    # # print(uniqueNames)
    # print('-----------------')
    # print(t)
    

    # def dd(n):
    #     # print(n)
    #     for i,j in n.items():
    #         # print(n[str(i)],j)
    #         if j in n[str(i)].values:
    #             n.pop(str(i))
    #             return dd(n)

    # dd(json_data['ssn_variations'])

    # size=len(json_data['ssn_variations'])


import json
with open('dit.json', 'r') as j:
    json_data = json.load(j)
    temp={}
    for i,j in json_data['ssn_variations'].items():
        if j not in temp.values():
            temp[i]=j
    # print(temp)
    json_data['ssn_variations'].clear()
    json_data['ssn_variations']=temp
    print(json_data)

    out_file = open("myfile.json", "w")
    json.dump(json_data, out_file, indent=4)
    out_file.close()



