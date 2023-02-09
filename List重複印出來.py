sample_list = [1,3,1,2,2,4,5,3]
count_list = []

for index, value in enumerate(sample_list):
    if sample_list.count(value) > 1 and  value not in count_list :
        count_list.append(value)

print(sorted(count_list))