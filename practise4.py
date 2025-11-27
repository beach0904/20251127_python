name = ["Alice", "Bob", "Charlie", "David", "Eva"]
nums = [11, 43, 69, 100, 88]
Alice = ["'Alice",60,89,77,90,65,90]

print(name) #顯示整個串列
name.append("Frank") #在串列最後新增元素
print("After append:", name)
name.insert(2, "Zara")  #在索引值2的位置插入元素
print("After insert at index 2:", name)
name.remove("Bob")  #移除指定元素
print("After removing 'Bob':", name)
name.pop(1) #移除索引值1的元素
print("After popping index 1:", name)
print("-----------------------------------------------------------------------------")

print("顯示nums串列:", nums) #顯示整個串列
nums.reverse()  #將串列反轉（就地修改，回傳 None）
print("幫nums反轉排序:", nums)
nums.sort()  #將串列由小到大排序（就地修改，回傳 None）
print("幫nums由小到大排序:", nums)
nums.sort(reverse=True)  #將串列由大到小排序（就地修改，回傳 None）
print("幫nums由大到小排序:", nums)
sorted_nums = sorted(nums)  #使用sorted函式排序，原串列不變
print("使用sorted函式排序:", sorted_nums)
print("-----------------------------------------------------------------------------")

suject = len(Alice)  #計算串列長度
score_max = max(Alice[1:])  #計算串列中最大值
score_min = min(Alice[1:])  #計算串列中最小值
i = Alice.index(score_max)  #尋找最大值的索引位置
l = Alice.index(score_min)  #尋找最小值的索引位置
print(f"愛麗絲最高考了{score_max}分,在第{i}個位置 對低分是{score_min}分,在第{l}個位置")
search_score = 90
k = Alice.count(search_score)  #計算指定元素在串列中出現的次數
print(f"愛麗絲有{k}科考了{search_score}分")