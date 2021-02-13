from random import randint
listComp = [randint(1,5) for i in range(10)]
print("Ex 01: ", listComp)

numberList = [[1,2,3],[4,5,6],[7,8,9]]
newList = [ ele 
            for subList in numberList 
                for ele in subList]
print("Ex 02: ", newList)