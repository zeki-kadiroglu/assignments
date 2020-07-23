sentence = input("enter sentence : ")
lst = list(sentence)
my_dic = {}
for i in lst:
    for j in lst:
        my_dic[i]= [lst.count(i)]


print(my_dic)
