#clear
attendees = ["Aravind","sai","praveen"]
print(attendees.clear())
print(type(attendees))
print(attendees)

#delete
attendees = ["sai","pavan","prakesh"]
del attendees[0]
print(attendees)

#example
attendee1 = input("Enter Attendee Name:")
attendee2 = input("Enter Attendee Name:")
attendee3 = input("Enter Attendee id :")
attendees=[]
attendees.append(attendee1)
attendees.append(attendee2)
attendees.append(attendee3)
print(attendees)

#sort list
lst = [100, 90, 88, 72, 66, 52, 40, 33, 28, 15, 9, 1]
lst.sort()
print(lst)

#reverse
lst = [10000,1000, 100, 10]
lst.reverse()
print(lst)

#tuple
# implicit
tpl = (1, 2, 3, 4, 5)
print(tpl)
print(type(tpl))

#explicty
tpl = tuple((1, 2, 3, 4, 5))
print(tpl)
print(type(tpl))

#data annotatoion
tpl:tuple = 1,2,3,4
print(tpl)


#count
tpl = tuple((1, 2, 3, 2))
print(tpl.count(2))

#index
tpl = tuple((1, 2, 3, 1))
print(tpl.index(3))

#example
tpl = tuple((1, 2, 3, 1))
lst = list(tpl)
print(type(lst))



#sort function with out using sorting method
l1 = [76, 23, 45, 12, 54, 9]
print("Original List:", l1)
for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j], l1[i]
print("Sorted List", l1)