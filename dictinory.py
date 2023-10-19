#dictionay
#implicit
#syntax:variableName={key:value,key:value}
userDetails = {'firstName': 'kumar', 'lastName': 'Aravind', 'Email': 'aravind111@gmail.com'}
print(type(userDetails))

#Explicit

#syntax:variableName=dict({key:value,key:value})

userDetails = dict({'firstName': 'kumar', 'lastName': 'Aravind', 'Email': 'aravind111@gmail.com'})
print(type(userDetails))

#datatype/Variable Annotation
#syntax:variableName:dict={key:value,key:value}
userDetails:dict = {'firstName': 'Arvind', 'lastName': 'swmai', 'Email': 'Aravind@gmail.com'}
print(type(userDetails))