mydict = {

  "brand" : "Mercedes",
  "model" : "S550",
  "model" : "GLE 63S",
  "seats" : 5,
  "year"  : 2024

}
print(mydict) #Output: {'brand': 'Mercedes', 'model': 'GLE 63S', 'seats': 5, 'year': 2024}

print(mydict["year"]) #Output: 2024
                            #The values in dictionary items can be of any data type:
                            #NB duplicates are not allowed or are rather ignored
                            # use the len() function to get the length
print(len(mydict))  #Output: 4
print(type(mydict)) #Output: < class 'dict' >

#Use the dict() constructor to make a dictionary.
simpledict = dict(name = "Jason", age = 30, country = "Kenya", job = "AI engineer")
print(simpledict)   #Output: {'name': 'Jason', 'age': 30, 'country': 'Kenya', 'job': 'AI engineer'}

x = print(simpledict.get("age")) #Output: 30

#The keys() method will return a list of all the keys in the dictionary
x = print(simpledict.keys())  #Output: dict_keys(['name', 'age', 'country', 'job'])


mysample = {
    "hobby": "footbal",
    "career": "tech",
    "car": "BMW",
    "salary": "3M"
}

mysample["house"] = "mansion"  
print(mysample)     #Output: {'hobby': 'footbal', 'career': 'tech', 'car': 'BMW', 'salary': '3M', 'house': 'mansion'}

x = mysample.values()
print(x)            #Output: dict_values(['footbal', 'tech', 'BMW', '3M', 'mansion'])

y = mysample.items()    # => The items() method will return each item in a dictionary, as tuples in a list.
print(y)            #Output: dict_items([('hobby', 'footbal'), ('career', 'tech'), ('car', 'BMW'), ('salary', '3M'), ('house', 'mansion')])

if "salary" in mysample:
    print("All set!!")  #Output: All set!!
z = print(mysample.get("career")) #Output: tech         # get() method dictionary.get(keyname, value)

mysample.update({"hobby": "swimming"}) 
print(mysample)          #Output: {'hobby': 'swimming', 'career': 'tech', 'car': 'BMW', 'salary': '3M', 'house': 'mansion'}

mysample.update({"fashion": "swaggy"})
print(mysample)         #Output: {'hobby': 'swimming', 'career': 'tech', 'car': 'BMW', 'salary': '3M', 'house': 'mansion', 'fashion': 'swaggy'}

mysample.popitem()
print(mysample)   #Output: {'hobby': 'swimming', 'career': 'tech', 'car': 'BMW', 'salary': '3M', 'house': 'mansion'}    
                 #NB: Removes item that was lastly added

del mysample ["house"]
print(mysample)    #Output {'hobby': 'swimming', 'career': 'tech', 'car': 'BMW', 'salary': '3M'}
            #NB; del can remove the entire dict but will cause an error, in such cases, clear() method


#loops
mydict = {

  "brand" : "Mercedes",
  "model" : "S550",
  "model" : "GLE 63S",
  "seats" : 5,
  "year"  : 2024

}
for x in mydict:
    print(x) #Output:brand
              #model
              #seats
              #year

for x in mydict.keys():
    print(x)    #brand
                # model
                # seats
                # year

for x in mydict.values():
    print(x)   #Output: #Mercedes
                        # GLE 63S
                        # 5
                        # 2024

for x, y in mydict.items():
    print(x, y)   # Output: #brand Mercedes
                            # model GLE 63S
                            # seats 5
                            # year 2024