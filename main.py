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