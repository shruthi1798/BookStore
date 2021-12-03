
n =int(input("Enter the number of books to be stored \n"))
d =int(input("\n Enter the discount provided for book store in % \t"))
d_tit= {} 
d_aut= {} 
d_price= {}
d_ncop= {} 
d_sc1= {} 
d_sc2= {}
d_tc = {}
for i in range (n):
    id = input("\nEnter the book id number\n")
    print("\nEnter the details of the books to be stored\n")
    title = input("Book title\t")
    author = input("Author name\t")
    price = input("Price of the book\t")
    copies =input("Total number of copies\t")
    ship_cost1 = input("Shipping cost for the first copies of books\t")
    ship_cost2 = input("Additional shipping cost for the second  copies of books in % \t")
    
    print("\n")

    d_tit[id] =title 
    d_aut[id] =author
    d_price[id] = float(price)
    d_ncop[id] = copies
    d_sc1[id] = int(ship_cost1)
    d_sc2[id] = int(ship_cost2)
    c = d_price[id] *  d_sc1[id] * d_sc2[id] * d 
    d_tc[id] = float(c)


while True:
  print("\nBOOKSTORE MENU")  
  print("1. Total wholesale cost")  
  print("2. Sort books as per a) author names and b) cost ")  
  print("3. Exit")  
  choice = int(input("Enter the Choice:\t"))  
  if choice == 1:  
    print("\nTotal cost for the given title book \n " )
    print(d_tc)

  elif choice == 2:  
    print("\nSorted list of the books as per the author names")
    print(sorted(d_aut.items(), key =
             lambda kv:(kv[1], kv[0])))   
    print("\nSorted list of the books as per the cost")
    print(sorted(d_tc.items(), key =
             lambda kv:(kv[1], kv[0])))  
    
  elif choice == 3:  
    
    print("End")
    break
  else :
    print("wrong choice")
