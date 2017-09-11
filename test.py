# coding:utf-8
import itchat

itchat.auto_login()
#itchat.send('This is Mingfeng', toUserName='filehelper')
friends = itchat.get_friends(update=True)[0:]
male = female = other = 0

for i in friends[1:]:
    print i
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

total = len(friends[1:])

print("total is %d" % total)

print("male:%.2f%%" %(float(male)/total*100) + "\n" +
      "female:%.2f%%" %(float(female)/total*100) + "\n" +
      "unknown:%.2f%%" %(float(other)/total*100))



