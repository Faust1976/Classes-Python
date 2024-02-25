def replace_rotten_fruits(fruit_list):

      fresh_fruits = []

      for fruit in fruit_list:

          if "rotten" in fruit.lower():

 

              fresh_fruits.append(fruit.replace("rotten", ""))

          else:

              fresh_fruits.append(fruit)

 

          return fresh_fruits

 

 

      fruit_list = ["apple", "Banana", "apple"]

      fresh_list = replace_rotten_fruits(fruit_list)

 

      print(fresh_list)
