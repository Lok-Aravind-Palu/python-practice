dictionary = {
      "Name": "Aravind",
      "ntId": "anages132",
      "password": "Acomcast132",
      "Days": 750
     }

try:
    last_name = dictionary["last_name"]
except:
    print("Not found")
finally:
    print("code executed")

#You can add two lists
dic1 = [1,2,3,4,5,6]
dic2 = ["a","s","d"]

listost = dic1 + dic2
print(listost)

#Exception

dictionary["Last_name"] = "Paluvadi"

try:
    last_name = dictionary["Last_name"]
    add_lastname = 24 + last_name
except KeyError:
    print("This is for not able give a value which is not there in dictionary")
except TypeError as error:
    print("This is for not able to add the string and integer")
    print(error)
except Exception:
    print("This is for any type of exception")
finally:
    print("This code has been executed")

