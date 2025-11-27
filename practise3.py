testname1 = "Kevin Lin"
testname2 = "Jack Ma"
tastpassword = "abcdefGHIJKL123456789"
tastemail = "xxxxxx@gmail.com"


print("顯示測試1名字:",testname1)  
#顯示字串
print("將字串轉換為小寫:",testname1.lower())
#將字串轉換為小寫
print("將字串的每個單字首字母大寫:",testname1.title())
#將字串的每個單字首字母大寫
print("將字串轉換為大寫:",testname1.upper())
#將字串轉換為大寫
print("將字串的大寫轉換為小寫，小寫轉換為大寫:",testname1.swapcase())
#將字串的大寫轉換為小寫，小寫轉換為大寫
print("-----------------------------------------------------------------------------")


print("顯示測試2名字:",testname2)  #顯示字串
print("去除名字左邊空白:",testname2.lstrip())
#去除名字左邊空白
print("去除名字右邊空白:",testname2.rstrip())
#去除名字右邊空白
print("去除名字左右兩邊空白:",testname2.strip())
#去除名字左右兩邊空白
print("將名字空白以星號取代空白:",testname2.replace(" ","*"))
#將名字空白以星號取代空白
print("將名字置中對其:",testname2.center(20))
#將名字置中對其
print("將名字靠左對其:",testname2.ljust(20))
#將名字靠左對其
print("將名字靠右對其:",testname2.rjust(20))
#將名字靠右對其 
print("將名字設定長度,多餘空間補0:",testname2.zfill(20))
#將名字設定長度,多餘空間補0
print("-----------------------------------------------------------------------------")

print("顯示測試密碼:",tastpassword)
print("密碼是否全是小寫:",tastpassword.islower())
#密碼是否全是小寫
print("密碼是否全是大寫:",tastpassword.isupper())
#密碼是否全是大寫
print("密碼是否全是字母:",tastpassword.isalpha())
#密碼是否全是字母
print("密碼是否全是數字:",tastpassword.isdigit())
#密碼是否全是數字
print("密碼是否全是字母和數字:",tastpassword.isalnum())
#密碼是否全是字母和數字
print("-----------------------------------------------------------------------------")

print("顯示測試信箱:",tastemail)
print("信箱是否是以xxx開頭:",tastemail.startswith("xxx"))
#信箱是否是以xxx開頭
print("信箱是否是@gmail.com結尾:",tastemail.endswith("@gmail.com"))
#信箱是否是@gmail.com結尾


