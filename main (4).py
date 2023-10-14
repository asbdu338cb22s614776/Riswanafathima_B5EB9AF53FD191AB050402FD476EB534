def linearsearchproduct(productlist,targetproduct):
  indices=[]
  for index,product in enumerate(productlist):
     if product==targetproduct:
       indices.append(index)
  return indices
products=["bangles","chain","earings","bangles","ring","bangles"]
target="bangles"
target2="saree"
result=linearsearchproduct(products,target)
print(result)
  