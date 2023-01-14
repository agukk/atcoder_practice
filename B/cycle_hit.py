s_list = [input() for i in range(4)]

result = 'No' if len(s_list) != len(set(s_list)) else 'Yes'
print(result)