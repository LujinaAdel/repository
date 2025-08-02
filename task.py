
# # my_dict =("apple ,watermalon ,pomegranate")
# # print(my_dict)


# # mystring = "i love py"
# # print(mystring[0])
# # print(mystring [-7] )
# # print( my_dict [0:5])
# # print( mystring [3::2])


# # a= "     I love python     "
# # print(a.strip())
# # print(a.rstrip())
# # print(a.lstrip())


# # a= "######I love python##"
# # print(a.strip("#"))
# # print(a.rstrip("#"))
# # print(a.lstrip("#"))

# # print(len (my_dict))

# # p="i Love 2d pY"
# # print(p.title())




# # p="i Love 2d pY"
# # print(p.capitalize())



# # #zfill
# # c,v,b="1","11","111"
# # print(c)
# # print(v)
# # print(b)



# # print(c.zfill(3))
# # print(v.zfill(3))
# # print(b.zfill(3))

# # g='logy'
# # print(g.upper())
# # print(g.lower())

# # f='i_ love_ logy_m'
# # print(f.rsplit("_",2))


# # y="logy lojina"
# # print(y.center(40,"i"))


# # j = "i love logy and python logy love python python love logy"
# # print(j.count("py",0,21))


# # name = 'logy'
# # a =16
# # r =10
# # print("my name is:%s and my adge is:%d" % (name , a))
# # print("my name is:%s and my adge is:%d and my rank is:%f" % (name , a , r))

# # mymoney=9000000000000000000000000000000
# # print("my money is: {:d}".format(mymoney))
# # print("my money is: {:_d}".format(mymoney))
# # print("my money is: {:,d}".format(mymoney))
# # print(f"my money in the bank is :{mymoney} and my adge is:{a}")
# # mycomplexnumber =3+7j
# # print(type(mycomplexnumber))
# # print(f"real part is: {mycomplexnumber.real}")

# # print(60+90)

# # myAwesomelist=["one","two","three" , 100,600]
# # print(myAwesomelist)
# # print(myAwesomelist[1])
# # print(type(myAwesomelist[1]))
# # print(myAwesomelist[2])
# # print(myAwesomelist[-1])
# # print(myAwesomelist[1:4])
# # print(myAwesomelist[5:-1])
# # print(type(myAwesomelist[3]))
# # print(myAwesomelist[::2])
# # print(myAwesomelist)
# # myAwesomelist[1] = 2
# # myAwesomelist[-1]=False
# # myAwesomelist[0:2] = []
# # print(myAwesomelist)

# # #append()
# # myfrind =["logy","mohamed","konafa"]
# # myoldfrind=["jac","koky","kamilia"]
# # myfrind.append("logina")
# # print(myfrind)

# # myfrind.append(myoldfrind)
# # print(myfrind)
# # print(myfrind[3][4])

# # y=[2,4,6,8,9,1,3,10]
# # y.sort()
# # print(y)
# # y.clear()
# # print(y)
# # k=[1,23,4,5,6,7,8]
# # c=k.copy()
# # k.append(5)
# # print(k)
# # print(c)

# # b=(1,3,4,6,8,9)
# # print(f"the position of index is :{b.index(3)}")

# # mysetone={"logy","1000"}
# # print(mysetone)

# # t={"ro","yo","co"}
# # o ={"lo","ko","to"}
# # print(t|o)
# # print(t.union(o))
# # t.add(5)
# # print(t)

# # lo={1,2,3,4,5}
# # lo.remove(1)
# # lo.discard(8)
# # print(lo)
# # #the remove will get error(if the num isn't found)
# # #discard won't get erorr

# # e={"adole",True,2,4,5,6,7}
# # print(e.pop())

# # d={1,2,3,4,5,6}
# # u={1,2,3}
# # print(d.issubset(u))
# # print(d.isdisjoint(u))

# # #dictionary
# # user={"name":"logy","age"  :36,"contry" :"konafa"}
# # print(user["age"])
# # print(user.keys())
# # print(user.values())

# # #two_dimensional dictionary
# # lang={"one":{"HTML","py","Css" "مش قاااادررر"}}
# # print(lang["one"])
# # print(len(lang["one"]))


# # users={"name" : "osama" }
# # print(users)
# # print(users.setdefault("age",36))
# # print(users)

# # #popitem()
# # member={"name": "logy" ,
# #         "age":16}
# # print(member)
# # member.update({"age" :43})
# # print(member.popitem())

# # view={"name": "logy" ,
# #         "age":16}
# # allitems=view.items()
# # print(view)
# # view["cont"]=89
# # print(allitems)


# # #boolen
# # print(bool("logg"))
# # print(bool(0))
# # print(bool(100))


# # #and
# # age =78
# # contry ="egypt"
# # rank =10
# # print(age>16 and contry == "egypt" and rank>0)
# # print(age>100 and contry == "eg" and rank>100)

# # #or
# # print(age>16 or contry == "egypt" or rank>0)
# # print(age>300 or contry == "ept" or rank>700)

# # #شقلب الكلام 
# # print(age >13)
# # print(not age >13)



# # fName= input("what\'s is your first Name?")
# # mname=input("what\'s is your middle Name?")
# # lname=input("what\'s is your last Name?")

# # fName= fName.capitalize().strip()
# # mname= mname.capitalize().strip()
# # lname= lname.capitalize().strip()

# # print(f"hello {fName} {mname :.1s} {lname} happy to see you")


# # email="lujinaadel@gmail.com"
# # # print(email.index("@"))
# # print(email[0:email.index("@")]) #very important
# # print(email[:12])
# #..............................................................
# # email="Konafa @ gmail.com"
# # print(email[:7])
# # print(email[:email.index("@")])
# # .............................................................

# # Uname ="logy"
# # Cname="py"
# # Cprice=100 
# # Cdiscont = 30
# # ucontry="eg"

# # if ucontry=="egypt":
# #     print(f"hello{Uname} bec. you 're from {ucontry}")
# #     print(f"hello{Uname} the course \'{Cname}\' price :{Cprice} but we have discont{Cprice - Cdiscont}")

# # elif ucontry=="KSA":
# #       print(f"hello{Uname} bec. you 're from {ucontry}")
# #       print(f"hello{Uname} the course \'{Cname}\' price :{Cprice} but we have discont{Cprice - Cdiscont}")

# # else:
# #      print(f"hello{Uname} bec. you 're from {ucontry}")
# #      print(f"hello{Uname} the course \'{Cname}\' price :{Cprice} but we have discont{Cprice - 80}")   


# # contry ="j"
# # if contry=="UK":
# #     print(f"the weather in {contry} us 14")

# # else:
# #     print("contry isn't found")

# # move=18
# # age=4
# # if age < move :
# #     print("go out")
# # else:
# #     print('move')


# # name="logy"
# # print("l" in name)



# # admins = ["logy","mohammed","mostafa"]


# # name = input("type your name:")

# # if name in admins:
# #     print("u r admin")
# #     print(f"hello{name}welcome back")
# #     option=input("delete or update:")
# #     print(option)
# #     if option =="update":
# #         thenewname = input("the new name:")
# #         admins[admins.index("logy")] = "logina"
# #         print(admins)
# #     elif option =="delete":
# #         admins.remove(name)
# #         print(admins)
# #     else:
# #         print("wrong writte")



# # else:
# #     print("u aren't admin")
# #     admins.append(name)

# # a = 0
# # while a<10:
# #         print(a)
# #         a +=1



# # # the first cocept to the while loop (old)
# # tries=4
# # mainpassword="logy@56"
# # inputpasword= input("writte your password:")

# # while inputpasword !=mainpassword :
# #     tries -=1
# #     print(f"wrong password ,{tries} chance left")
# #     inputpasword= input("writte your password:")
# #     if tries ==0:
# #         print("all tries is finshed")
# #         break



# # # the scond concept to while loop(modern)تستخدم احسن في الشغل
# # tries=4
# # mainpassword="logy@56"
# # inputpasword= input("writte your password:")

# # while inputpasword !=mainpassword :
# #     tries -=1
# #     print(f"wrong password ,{"last" if tries ==0 else tries} chance left")
# #     inputpasword= input("writte your password:")
# #     if tries ==0:
# #         print("all tries is finshed")
# #         break

# # # take care about spaaaaaaaaaace(else بره ال while)
# # else:
# #         print("password is correct")




# # # FORLOOP
# # number=[1,2,3,4,5,6,7,8,9]
# # for num in number:
# #     print(num)
# #     if num % 2==0:
# #         print(f"the number {num} is even")
# #     else:
# #         print(f"the nimber{num}is odd")



# # # task 
# # eat=["bashamell","boftak","creamcaramel"]
# # print(eat)
# # food=input("choose one type of food :")
# # if food=="bashamell":
# #     print("good")
# # else:
# #     print("fen el bashamell")


# # letter
# # myname="logy"
# # for letter in myname:
# #     print(f"[{letter.upper}]")


# # # Range
# # myrange=range(1,200)
# # for num in myrange:
# #     print(num)

# # myskills={
# #     "html": "89%",
# #     "python":"67%",
# #     "php": "80%",
# #     "jsl": "100%"
# # }
# # # print(myskills['jsl'])
# # # print(myskills.get("python"))
# # for skill in myskills:
# #     # print(skill)
# #    print(f" {skill}:{myskills[skill]}")

# peoples={
#     "logy":{
#         "html": "80%",
#           "py": "100%",
#          "php": "40%",
#           "css": "99%",
#            "js": "70%",
#             "go": "30%",
#     },
#     "Bashamall":{
#         "bashamall":"99%",
#         "pasta":"40%",
#         "meat":"50%",
#         "cheese":"60%"
#     },
# }

# # print(peoples["logy"]["css"])

# # nested loop
# for name in peoples:
#     print(f"skills and prograss for {name} is :")
#     for skill in peoples[name]:
#         print(f"{skill}= {peoples[name][skill]}")



# continue (make skip for .....)
# 1,2,3,4,5,6    continue   1,2,4,5,6
# break (بتوقف لحد .......)
# 1,2,3,4,5,6   break   1,2,3
# pass (ماشي الدنيا)
# for name in names:
    # pass             (حتمشي عادي)

# def function_name ():
#     return "hello py"
# dstsfromfunction=function_name()
# print(dstsfromfunction)
# def say_hello(n):
#     print (f"hello {n}")

# say_hello("logy")


# def addition(n1,n2):
#     print(n1+n2)

# addition(100,300)

# def addition(n1,n2):
#     if type(n1)!= int or type(n2)!=int :
#         print("only int allow")
#     else:
#         print(n1+n2)

# addition(100,300)
# addition("logy","Lujina")


# print((1,2,3,4,5,6,7,8))
# mylist=[1,2,3,4,5,6,7,8]
# print(mylist)
# print(*mylist)

# def say_hello(people , *skills):
#     print(f"hello {people} your skills are :")
#     for skill in skills:
#         print(skill)

# say_hello("logy","py","php","sql")
# say_hello("mohamed","js","py")

# # TASK TEST:
# def say_py(*numbers):
#     for num in numbers:
#         print(f"the number: {num}")
# say_py(1,2,3)

# def say_hello(name , age , contry = "unknown"):
#     print(f"hello{name} your age is : {age} your contry :{contry}")

# say_hello("lujina", 16 , "jordon")
# say_hello("logy", 10 ) # error في حاله اننا مش كاتبين unknown
# def show_skills(*skills):
#     print(type(skills))
#     for skill in skills:
#         print(f"your skill is :{skill}")
# show_skills("html","css","py")

# # PACKING , UNPACKING
# def show_skills(**skills):
#     print(type(skills))
#     for skill , value in skills.items():
#         print(f"your skill is :{skill} = {value}")
# show_skills (HTML="50%",CSS ="70%",PY="100%")


# # as dictionary
# myskills={"HTML":"50%",
#           "CSS" :"70%",
#           "PY":"100%"
# }
# def show_skills(**skills):
#     print(type(skills))
#     for skill , value in skills.items():
#         print(f"your skill is :{skill} = {value}")
# show_skills (**myskills)



# # revsion
# myskills={"HTML":"50%",
#           "CSS" :"70%",
#           "PY":"100%"}
# def show_skills(name,*skills ,**skillswhithprogres):
#     print(f"hello {name} \n skills without progress: ")
#     for skill in skills:
#         print(f"- {skill}")
# show_skills("logy", "html" , "py" , "css" , "js")
# for skill_key , skill_value in skillswhithprogres.items():
#     print(f"-{skill_key} = {skill_value}")

# show_skills("osama")

# scope
# r =1
# def one():
#     print(f"print variable from function scope {r}")

# print(f"print variable from global scope {r}")
# one()
"""
recursion
x = "wwooooooooorllddd"
def cleanworld(word):
    if len(word) ==1 :
        return word
    if word[0] == word[1]:
        return cleanworld(word[1:])
    return word[0] + cleanworld(word[1:])

print(cleanworld("wwooooooooorllddd"))
"""
# def say_hello(name):
#     return f"hello {name}"
# hello = lambda name : f"hello {name}"
# print(say_hello("logy"))
# print(hello("logina"))

# import logy
# print(logy.getcwd())

# file= open (r"C:\logy.text")

# mylist = ["logy","rodina","lujina"]
# myfile = open("C:\logy.text","w")
# myfile.writelines(mylist)

# x = [1 , 3,4,5,6,7]
# if all(x):
#     print("all true")

# else:
#     print("at least one element")
# x = [1 , 3,4,5,6,7]
# if any(x):
#     print("at least one true")

# else:
#     print("at least one element")

# a=1
# n=2
# print(id(a))
# print(id(n))

# print(list(range(0)))
# print(list(range(10)))
# print(list(range(0,40,2)))
# print(hello,logy sep="@")

######59___70#####



