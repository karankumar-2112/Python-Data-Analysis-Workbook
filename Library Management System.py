"""
Library Management System

member (mid, mname, maddress, mmobile)
book (bid, btitle, price, author)
borrow (mid, bid, days)

1- Add Member
2- View Members
3- Delete Member
4- Add Book
5- View Books
6- Update Book
7- Borrow Book
8- View All Borrowings
9- View Borrowings By Member
0- Exit
"""
#REQUIRED LIBRARIES
import pickle
import os
# A METHOD TO ADD MEMBER
def addMember():
    file = open('member.bin','ab')
    mid = input("\n\tEnter New Member ID : ")
    mname = input("\tEnter New Member Name : ")
    madd = input("\tEnter Member Address : ")
    mmob = input("\tEnter Member Mobile : ")
    pickle.dump(mid,file)
    pickle.dump(mname,file)
    pickle.dump(madd,file)
    pickle.dump(mmob,file)
    file.close()
    print("\n\tMEMBER ADDED SUCCESSFULLY!")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO VIEW ALL MEMBERS
def viewMembers():
    file = open('member.bin','rb')
    try:
        print("\nMID\tMNAME\tMADD\tMMOB\n")
        while True:
            for i in range(4):
                data = pickle.load(file)
                print(data,end="\t")
            print()
    except:
        pass
    file.close()
    print("\n\tHERE IS YOUR ALL MEMBER's")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO DELETE MEMBER
def deleteMember():
    file1 = open('member.bin','rb')
    file2 = open('temp.bin','ab')
    flag = 0
    mid =input("\n\tEnter Member ID To Delete : ")
    try:
        while True:
            data = pickle.load(file1)
            if data==mid:
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        pass
    file1.close()
    file2.close()
    os.remove('member.bin')
    os.rename('temp.bin','member.bin')
    if flag==1:
        print("\n\tMEMBER DELETED SUCCESSFULLY!")
    else:
        print("\tMEMBER NOT FOUND!")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO ADD BOOK
def addBook():
    file = open('books.bin','ab')
    bid = input("\n\tEnter New Book ID : ")
    btitle = input("\tEnter New Book Title : ")
    price = input("\tEnter Book Price : ")
    author = input("\tEnter Book Author Name : ")
    pickle.dump(bid,file)
    pickle.dump(btitle,file)
    pickle.dump(price,file)
    pickle.dump(author,file)
    file.close()
    print("\n\tBOOK ADDED SUCCESSFULLY!")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO VIEW BOOKS
def viewBooks():
    file = open('books.bin','rb')
    try:
        print("\nBID\t BNAME\t\tPRICE\t AUTHOR\n")
        while True:
            for i in range(4):
                data = pickle.load(file)
                print(data,end="\t ")
            print()
    except:
        pass
    file.close()
    print("\n\tHERE IS YOUR ALL BOOK's")
    input("\tPRESS ENTER TO CONTINUE...")
# A METHOD TO UPDATE BOOK's PRICE
def updateBook():
    file1 = open('books.bin','rb')
    file2 = open('update.bin','ab')
    flag = 0
    bid = input("\n\tEnter Book ID To Update Price : ")
    try:
        while True:
            data = pickle.load(file1)
            if data==bid:
                pickle.dump(data,file2)
                name = pickle.load(file1)
                print("\n\tName :",name)
                pickle.dump(name,file2)
                print("\tPrice :",pickle.load(file1))
                price = input("\n\tEnter New Price : ")
                pickle.dump(price,file2)
                author = pickle.load(file1)
                pickle.dump(author,file2)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        pass
    file1.close()
    file2.close()
    os.remove('books.bin')
    os.rename('update.bin','books.bin')
    if flag==1:
        print("\n\tPRICE UPDATED SUCCESSFULLY!")
    else:
        print("\tBOOK NOT FOUND!")
    input("\tPRESS ENTER TO CONTINUE!")

# A METHOD TO GET ALL MEMBER DETAIL's
def getMember(mid):
    memb = []
    file = open('member.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==mid:
                memb.append(data)
                for i in range(3):
                    memb.append(pickle.load(file))
    except:
        pass
    file.close()
    return memb
# A METHOD TO GET ALL BOOKS
def getbook(bid):
    book = []
    file = open('books.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==bid:
                book.append(data)
                for i in range(3):
                    book.append(pickle.load(file))
    except:
        pass
    file.close()
    return book
# A METHOD TO BORROW A BOOK
def borrowBook():
    mid = input("\n\tEnter Member ID : ")
    memb = getMember(mid)
    if len(memb)!=0:
        print("\n\tMember Name :",memb[1])
        print("\tMember Address :",memb[2])
        bid = input("\n\tEnter Book ID : ")
        book = getbook(bid)
        if len(book)!=0:
            print("\n\tBook Name :",book[1])
            print("\tBook Price :",book[2])
            qty = input("\n\tEnter The Quantity : ")
            print("\n\tTotal Bill :",float(qty)*float(book[2]))
            file = open('borrow.bin','ab')
            pickle.dump(mid,file)
            pickle.dump(bid,file)
            pickle.dump(qty,file)
            file.close()
            print("\n\tBOOK BORROWED SUCCESSFULLY!")
        else:
            print("\n\tBOOK NOT FOUND!")
    else:
        print("\n\tYOU ARE NOT REGISTERED AS MEMBER!")
    input("\tPRESS ENTER TO CONTINUE...")
#A METHOD TO VIEW ALL BORROWINGS
def viewBorrowings():
    file = open('borrow.bin','rb')
    try:
        print("\n\tMNAME\tBNAME\t BPRICE\t QTY\tAMOUNT\n")
        while True:
            memb = getMember(pickle.load(file))
            book = getbook(pickle.load(file))
            qty = pickle.load(file)
            if len(memb)!=0:
                print(f"\t{memb[1]}\t{book[1]}\t {book[2]}\t  {qty}\t{int(book[2])*int(qty)}")
    except:
        pass
    file.close()
    print("\n\tHERE IS ALL BORROWING!")
    input("\tPRESS ENTER TO CONTINUE...")
# A METHOD TO VIEW ALL BORROWINGS BY MEMBER ID
def viewBorrowingsByMid():
    mid = input("\n\tEnter Member ID : ")
    i = 1
    memb = getMember(mid)   
    if len(memb)!=0:
        file = open('borrow.bin','rb')
        try:
            while True:
                memb = getMember(pickle.load(file))
                book = getbook(pickle.load(file))
                qty = pickle.load(file)
                if len(memb)!=0:
                    if memb[0]==mid:
                        print("\n--------------------------------")
                        print("Order No.",i)
                        print("\tMember Name :",memb[1])
                        print("\tBook Name :",book[1])
                        print("\tBook Price :",book[2])
                        print("\tBook Quantity :",qty)
                        print("\tTotal Amount :",int(book[2])*int(qty))
                        print("\n--------------------------------")
                        i +=1
        except:
            pass
        file.close()
    else:
        print("\n\tMEMBER NOT FOUND ON THIS ID!")
    input("PRESS ENTER TO CONTINUE...")

# DASHBOARD
print("\n\t  Library Management System")
while True:
    print("\t-----------------------------")
    print("""    1- Add Member
    2- View Members
    3- Delete Member
    4- Add Book
    5- View Books
    6- Update Book
    7- Borrow Book
    8- View All Borrowings
    9- View Borrowings By Member
    0- Exit""")
    ch = int(input("\nEnter Your Choice : "))
    if ch==0:
        print("\n\t Thank You!")
        break
    elif ch==1:
        addMember()
    elif ch==2:
        viewMembers()
    elif ch==3:
        deleteMember()
    elif ch==4:
        addBook()
    elif ch==5:
        viewBooks()
    elif ch==6:
        updateBook()
    elif ch==7:
        borrowBook()
    elif ch==8:
        viewBorrowings()
    elif ch==9:
        viewBorrowingsByMid()
    else:
        print("\n\tWRONG CHOICE\n\t TRY AGAIN!")
        input("\nPRESS ENTER...")

