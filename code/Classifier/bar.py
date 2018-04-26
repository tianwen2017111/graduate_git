import matplotlib.pyplot as plt

num_list =  [1243274,1257898,1128623,1113008,662096,688665,747726,1163948,1044572,
    1122312,1052268,4380765,1913710,370000,602381,1095572,1317020,1489504,
    1126275,313902,1329717,1730803,775573];
x = range(1,len(num_list)+1)
# plt.bar(x, num_list, 1, color="lightskyblue")
plt.bar(x, num_list, 1, color="darkseagreen")
plt.show()