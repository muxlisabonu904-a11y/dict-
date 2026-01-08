import os
os.system("cls")
car={
    "brand": "chevrolet",
    "model": "malibu",
    "rang" : "qora",
    "narx" : 18_000,
    "probeg" : 15_000,

}

car['yil'] = 2025
print(car)
car["model"]= 'cobalt'
print(car["model"])


# 

# import os
# os.system("cls")
# car={
#     "brand": "chevrolet",
#     "model": "malibu",
#     "rang" : "qora",
#     "narx" : 18_000,
#     "probeg" : 15_000,

# }

# if "malibu" in car:
#     print("yes")
# else:
#     print("no")


# 


# for i in car: 
#     print(i, car[i])


#      (get)

# print (car.get('bran',"bunday kalit topilmadi!"))
# print(car["brand"]) 


#     keys

# print(car.keys())
#    || print(list(car.keys()))


# velius
# print(car.valius())



#    ---->
# if"malibu" in car.values():
#     print("yes")
# else:
#     print("no")

 # ---->



#   pop
# n=car.pop('narx')
# print(car)
# print(n)



# print(car.items())
# for k,v in car.itms():
#     print(k,v)


# copy 
# car2=car
# car3=car.copy()


# # popitime
# car["yil"]=2014
# print(car.popoitimes())
# print(car)



# #   update                                     
# car.update({"narx":15000, "probeg":2100000,"ranglar":['oq','pushti'], "yil":2021})
# print(car)