x=int(input("enetr in range 1 to 12: "))
n=["Jan","Feb","March","Apr","May","June","july","Aug","Sep","Oct","Nov","Dec"]

if x%2==0 and x!=2:
    print(n[x-1]," has 30 days")
elif x==2:
    print(n[x-1]," has 28 days")

else:
    print(n[x-1],"has 31 days")
