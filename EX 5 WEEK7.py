x = "list"
print("This is your shoppig list")
print("Press (ENTER) to exit the shopping list")

mylist = ""

while x != "":
    
    x = input("Add your products:")
    print("You added" , x)
    mylist = mylist+x+","

if x == "":
    print("Thanks for shopping")
    print("Your list = "+mylist)

