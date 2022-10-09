import json

final_dict = {}

with open('data.csv') as csv_file:
    for item in csv_file.readlines():
        item = item.strip().split(',')
        if item[0] in final_dict.keys():
            final_dict[item[0]]["people"].append(item[1])
            final_dict[item[0]]["count"] += 1
        elif item[0] not in final_dict.keys():
            final_dict[item[0]] = {"people": [item[1]], "count": 1}
        

result_dict = json.dumps(final_dict, indent=2, default=str)
print(result_dict)
