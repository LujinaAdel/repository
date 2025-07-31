
# my_dict =("apple ,watermalon ,pomegranate")
# print(my_dict)


# mystring = "i love py"
# print(mystring[0])
# print(mystring [-7] )
# print( my_dict [0:5])
# print( mystring [3::2])


# a= "     I love python     "
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())


# a= "######I love python##"
# print(a.strip("#"))
# print(a.rstrip("#"))
# print(a.lstrip("#"))

# print(len (my_dict))

# p="i Love 2d pY"
# print(p.title())




# p="i Love 2d pY"
# print(p.capitalize())



# #zfill
# c,v,b="1","11","111"
# print(c)
# print(v)
# print(b)



# print(c.zfill(3))
# print(v.zfill(3))
# print(b.zfill(3))

# g='logy'
# print(g.upper())
# print(g.lower())

# f='i_ love_ logy_m'
# print(f.rsplit("_",2))


# y="logy lojina"
# print(y.center(40,"i"))


# j = "i love logy and python logy love python python love logy"
# print(j.count("py",0,21))


# name = 'logy'
# a =16
# r =10
# print("my name is:%s and my adge is:%d" % (name , a))
# print("my name is:%s and my adge is:%d and my rank is:%f" % (name , a , r))

# mymoney=9000000000000000000000000000000
# print("my money is: {:d}".format(mymoney))
# print("my money is: {:_d}".format(mymoney))
# print("my money is: {:,d}".format(mymoney))
# print(f"my money in the bank is :{mymoney} and my adge is:{a}")
# mycomplexnumber =3+7j
# print(type(mycomplexnumber))
# print(f"real part is: {mycomplexnumber.real}")

# print(60+90)

# myAwesomelist=["one","two","three" , 100,600]
# print(myAwesomelist)
# print(myAwesomelist[1])
# print(type(myAwesomelist[1]))
# print(myAwesomelist[2])
# print(myAwesomelist[-1])
# print(myAwesomelist[1:4])
# print(myAwesomelist[5:-1])
# print(type(myAwesomelist[3]))
# print(myAwesomelist[::2])
# print(myAwesomelist)
# myAwesomelist[1] = 2
# myAwesomelist[-1]=False
# myAwesomelist[0:2] = []
# print(myAwesomelist)

# #append()
# myfrind =["logy","mohamed","konafa"]
# myoldfrind=["jac","koky","kamilia"]
# myfrind.append("logina")
# print(myfrind)

# myfrind.append(myoldfrind)
# print(myfrind)
# print(myfrind[3][4])

# y=[2,4,6,8,9,1,3,10]
# y.sort()
# print(y)
# y.clear()
# print(y)
# k=[1,23,4,5,6,7,8]
# c=k.copy()
# k.append(5)
# print(k)
# print(c)

# b=(1,3,4,6,8,9)
# print(f"the position of index is :{b.index(3)}")

# mysetone={"logy","1000"}
# print(mysetone)

# t={"ro","yo","co"}
# o ={"lo","ko","to"}
# print(t|o)
# print(t.union(o))
# t.add(5)
# print(t)

# lo={1,2,3,4,5}
# lo.remove(1)
# lo.discard(8)
# print(lo)
# #the remove will get error(if the num isn't found)
# #discard won't get erorr

# e={"adole",True,2,4,5,6,7}
# print(e.pop())

# d={1,2,3,4,5,6}
# u={1,2,3}
# print(d.issubset(u))
# print(d.isdisjoint(u))

# #dictionary
# user={"name":"logy","age"  :36,"contry" :"konafa"}
# print(user["age"])
# print(user.keys())
# print(user.values())

# #two_dimensional dictionary
# lang={"one":{"HTML","py","Css" "مش قاااادررر"}}
# print(lang["one"])
# print(len(lang["one"]))


# users={"name" : "osama" }
# print(users)
# print(users.setdefault("age",36))
# print(users)

# #popitem()
# member={"name": "logy" ,
#         "age":16}
# print(member)
# member.update({"age" :43})
# print(member.popitem())

# view={"name": "logy" ,
#         "age":16}
# allitems=view.items()
# print(view)
# view["cont"]=89
# print(allitems)


# #boolen
# print(bool("logg"))
# print(bool(0))
# print(bool(100))


# #and
# age =78
# contry ="egypt"
# rank =10
# print(age>16 and contry == "egypt" and rank>0)
# print(age>100 and contry == "eg" and rank>100)

# #or
# print(age>16 or contry == "egypt" or rank>0)
# print(age>300 or contry == "ept" or rank>700)

# #شقلب الكلام 
# print(age >13)
# print(not age >13)



# fName= input("what\'s is your first Name?")
# mname=input("what\'s is your middle Name?")
# lname=input("what\'s is your last Name?")

# fName= fName.capitalize().strip()
# mname= mname.capitalize().strip()
# lname= lname.capitalize().strip()

# print(f"hello {fName} {mname :.1s} {lname} happy to see you")


# email="lujinaadel@gmail.com"
# # print(email.index("@"))
# print(email[0:email.index("@")]) #very important
# print(email[:12])
#..............................................................
# email="Konafa @ gmail.com"
# print(email[:7])
# print(email[:email.index("@")])
# .............................................................

# Uname ="logy"
# Cname="py"
# Cprice=100 
# Cdiscont = 30
# ucontry="eg"

# if ucontry=="egypt":
#     print(f"hello{Uname} bec. you 're from {ucontry}")
#     print(f"hello{Uname} the course \'{Cname}\' price :{Cprice} but we have discont{Cprice - Cdiscont}")

# elif ucontry=="KSA":
#       print(f"hello{Uname} bec. you 're from {ucontry}")
#       print(f"hello{Uname} the course \'{Cname}\' price :{Cprice} but we have discont{Cprice - Cdiscont}")

# else:
#      print(f"hello{Uname} bec. you 're from {ucontry}")
#      print(f"hello{Uname} the course \'{Cname}\' price :{Cprice} but we have discont{Cprice - 80}")   


# contry ="j"
# if contry=="UK":
#     print(f"the weather in {contry} us 14")

# else:
#     print("contry isn't found")

# move=18
# age=4
# if age < move :
#     print("go out")
# else:
#     print('move')


# name="logy"
# print("l" in name)



# admins = ["logy","mohammed","mostafa"]


# name = input("type your name:")

# if name in admins:
#     print("u r admin")
#     print(f"hello{name}welcome back")
#     option=input("delete or update:")
#     print(option)
#     if option =="update":
#         thenewname = input("the new name:")
#         admins[admins.index("logy")] = "logina"
#         print(admins)
#     elif option =="delete":
#         admins.remove(name)
#         print(admins)
#     else:
#         print("wrong writte")



# else:
#     print("u aren't admin")
#     admins.append(name)

# a = 0
# while a<10:
#         print(a)
#         a +=1

















      



    




