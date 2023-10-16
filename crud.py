#curd operations
#create / add data to list
lst = ["Aravind",1,True]
print(lst)

#Append()
lst :lst=["Aravind","swamai","kumar"]
lst.append("yuv")
print(lst)

#insert()
attendeess=["Aravind","vamsi","prasad"]
attendeess.insert(3,"kumar")
print(attendeess)

#count()
attendeess=["Aravind","kumar","vamsi","kumar","kumar"]
print(attendeess.count("kumar"))
print(attendeess.count("abc"))

#index().
attendeess=["kumar","vamsi","Aravind"]
print(attendeess.index("Aravind"))

#count()
attendeess = ["navya","vamsi","prasad","vamsi"]
if(attendeess.count("bablu")>0):
    print(attendeess.index("bablu"))

#update by using index
attendeess=["swami","Aravind","prasad"]
attendeess[1]= "Aravind kumar"
print(attendeess)

#extend
attendeess=["Aravind","vamsi","prasad"]
attendeess1=["kumar"]
attendeess.extend(attendeess1)
print(attendeess)

#delete
attendeess=["Aravind","vamsi","swami"]
attendeess.remove("swami")
print(attendeess)

#pop with index
attendeess=["Aravind","vamsi","prasad", "swami"]
attendeess.pop(3)
print(attendeess)

#pop without index
attendeess=["Aravind","vamsi","prasad"]
attendeess.pop()
attendeess.pop()
print(attendeess)