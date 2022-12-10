import psycopg2
from psycopg2 import Error


pwd = 'Batman1.' #Enter your local password here.

#this is used to connect to a database
try:
    connect = psycopg2.connect(user="postgres", password=pwd, host="127.0.0.1", port="5432", database="bookstore")
    print("Connection was successful to PostgreSQL")

    #required to perfrom database operations
    cur = connect.cursor()
    #this is used to drop any existing tables.
    dropTables = ''' DROP TABLE IF EXISTS Book CASCADE;
                    DROP TABLE IF EXISTS Author CASCADE;
                    DROP TABLE IF EXISTS Users CASCADE;
                    DROP TABLE IF EXISTS Publisher CASCADE;
                    DROP TABLE IF EXISTS CheckoutBasket CASCADE;
                    DROP TABLE IF EXISTS Orders CASCADE;
                    DROP TABLE IF EXISTS Report CASCADE;
                    DROP TABLE IF EXISTS Owner CASCADE;
                    DROP TABLE IF EXISTS searches;
                    DROP TABLE IF EXISTS addBook;
                    DROP TABLE IF EXISTS written;
                    DROP TABLE IF EXISTS published;
                    DROP TABLE IF EXISTS register;
                    DROP TABLE IF EXISTS placeOrder;
                    DROP TABLE IF EXISTS track;
                    DROP TABLE IF EXISTS ship;
                    DROP TABLE IF EXISTS transfer;
                    DROP TABLE IF EXISTS recordsale;
                    DROP TABLE IF EXISTS gets;
                    DROP TABLE IF EXISTS adds;
                    DROP TABLE IF EXISTS remove;
                    DROP TABLE IF EXISTS sendemail;
    '''

    #this is used to create tables
    createTables = ''' CREATE TABLE IF NOT EXISTS Book(
                            bookID      INT             PRIMARY KEY,
                            bookname    VARCHAR(40)    NOT NULL,
                            authorName  VARCHAR(40)    NOT NULL,
                            ISBN        INT             NOT NULL,
                            genre       VARCHAR(100)    NOT NULL,
                            price       INT             NOT NULL,
                            pages       INT             NOT NULL
                        );

                        CREATE TABLE IF NOT EXISTS Author(
                            AuthID      INT             PRIMARY KEY,
                            AuthName    VARCHAR(40)    NOT NULL
                        );
                            
                        CREATE TABLE IF NOT EXISTS Users(
                            UserID          INT             PRIMARY KEY,
                            UserName        VARCHAR(40)    NOT NULL,
                            BillingInfo     VARCHAR(100)    NOT NULL,
                            ShippingInfo    VARCHAR(100)    NOT NULL,
                            PhoneNum        INT    NOT NULL
                        );
                        
                        CREATE TABLE IF NOT EXISTS CheckoutBasket(
                            CartID          INT             PRIMARY KEY,
                            bookName        VARCHAR(100)    NOT NULL,
                            bookQuantity    INT             NOT NULL,
                            totalPrice      INT             NOT NULL,
                            billingInfo     VARCHAR(100)    NOT NULL,
                            shippingInfo    VARCHAR(100)    NOT NULL
                        );

                        CREATE TABLE IF NOT EXISTS Orders(
                            OrderNumber     INT             PRIMARY KEY,
                            userName        VARCHAR(40)     NOT NULL,
                            userID          INT             NOT NULL,
                            ShipmentDate    DATE            NOT NULL
                        );

                        CREATE TABLE IF NOT EXISTS Report(
                            ReportID            INT         PRIMARY KEY,
                            TotalSales          INT         NOT NULL,
                            TotalExpenditure   INT         NOT NULL,
                            SalesperGenre       INT         NOT NULL,
                            SalesperAuthor      INT         NOT NULL
                        );

                        CREATE TABLE IF NOT EXISTS Owner(
                            OwnID               INT             PRIMARY KEY,
                            OwnerEmail          VARCHAR(40)     NOT NULL,
                            OwnerPhone          INT             NOT NULL,
                            OwnerName           VARCHAR(40)     NOT NULL,
                            BankAccount         INT             NOT NULL
                        );

                        CREATE TABLE IF NOT EXISTS Publisher(
                            PubID               INT         PRIMARY KEY,
                            PubName             VARCHAR(40)     NOT NULL,
                            Address             VARCHAR(100)     NOT NULL,
                            Email               VARCHAR(40)     NOT NULL,
                            PhoneNumbers        INT             NOT NULL,
                            BankingAccount      INT             NOT NULL
                        );

                        CREATE TABLE IF NOT EXISTS search(
                            bookID          INT,
                            UserID          INT,
                            FOREIGN KEY (bookID) REFERENCES Book (bookID),
                            FOREIGN KEY (UserID) REFERENCES Users (UserID)
                        );

                        CREATE TABLE IF NOT EXISTS addBook(
                            bookID          INT,
                            CartID          INT,
                            FOREIGN KEY (bookID) REFERENCES Book (bookID),
                            FOREIGN KEY (CartID) REFERENCES CheckoutBasket (CartID)
                        );

                        CREATE TABLE IF NOT EXISTS written(
                            bookID          INT,
                            AuthID          INT,
                            FOREIGN KEY (bookID) REFERENCES Book (bookID),
                            FOREIGN KEY (AuthID) REFERENCES Author (AuthID)
                        );

                        CREATE TABLE IF NOT EXISTS published(
                            bookID          INT,
                            PubID           INT,
                            FOREIGN KEY (bookID) REFERENCES Book (bookID),
                            FOREIGN KEY (PubID) REFERENCES Publisher (PubID)
                        );

                        CREATE TABLE IF NOT EXISTS register(
                            CartID          INT,
                            UserID          INT,
                            FOREIGN KEY (CartID) REFERENCES CheckoutBasket (CartID),
                            FOREIGN KEY (UserID) REFERENCES Users (UserID)
                        );

                        CREATE TABLE IF NOT EXISTS placeOrder(
                            CartID              INT,
                            OrderNumber         INT,
                            FOREIGN KEY (CartID) REFERENCES CheckoutBasket (CartID),
                            FOREIGN KEY (OrderNumber) REFERENCES Orders (OrderNumber)
                        );

                        CREATE TABLE IF NOT EXISTS track(
                            UserID              INT,
                            OrderNumber         INT,
                            FOREIGN KEY (UserID) REFERENCES Users (UserID),
                            FOREIGN KEY (OrderNumber) REFERENCES Orders (OrderNumber)
                        );

                        CREATE TABLE IF NOT EXISTS ship(
                            UserID              INT,
                            OrderNumber         INT,
                            shippingCompany     VARCHAR(40)     NOT NULL,
                            FOREIGN KEY (UserID) REFERENCES Users (UserID),
                            FOREIGN KEY (OrderNumber) REFERENCES Orders (OrderNumber)
                        );

                        CREATE TABLE IF NOT EXISTS transfer(
                            PubID              INT,
                            OrderNumber         INT,
                            FOREIGN KEY (PubID) REFERENCES Publisher (PubID),
                            FOREIGN KEY (OrderNumber) REFERENCES Orders (OrderNumber)
                        );

                        CREATE TABLE IF NOT EXISTS recordSale(
                            ReportID            INT,
                            OrderNumber         INT,
                            FOREIGN KEY (ReportID) REFERENCES Report (ReportID),
                            FOREIGN KEY (OrderNumber) REFERENCES Orders (OrderNumber)
                        );

                        CREATE TABLE IF NOT EXISTS gets(
                            ReportID        INT,
                            OwnID           INT,
                            FOREIGN KEY (ReportID) REFERENCES Report (ReportID),
                            FOREIGN KEY (OwnID) REFERENCES Owner (OwnID)
                        );

                        CREATE TABLE IF NOT EXISTS adds(
                            bookID          INT,
                            OwnID           INT,
                            FOREIGN KEY (bookID) REFERENCES Book (bookID),
                            FOREIGN KEY (OwnID) REFERENCES Owner (OwnID)
                        );

                        CREATE TABLE IF NOT EXISTS remove(
                            bookID          INT,
                            OwnID           INT,
                            FOREIGN KEY (bookID) REFERENCES Book (bookID),
                            FOREIGN KEY (OwnID) REFERENCES Owner (OwnID)
                        );

                        CREATE TABLE IF NOT EXISTS sendEmail(
                            PubID           INT,
                            OwnID           INT,
                            FOREIGN KEY (PubID) REFERENCES Publisher (PubID),
                            FOREIGN KEY (OwnID) REFERENCES Owner (OwnID)
                        );'''

    #insert into those tables.
    insertTables = ''' INSERT INTO Book (bookID, bookName, authorName,ISBN, genre, price, pages) values (1, 'Mujtabas Book1', 'Mujtaba' ,1001, 'Scary', 10, 423);
                    INSERT INTO Book (bookID, bookName, authorName, ISBN, genre, price, pages) values (2, 'Not Mujs Book1', 'Not Muj', 1002, 'Comedy', 20, 624);
                    INSERT INTO Book (bookID, bookName, authorName, ISBN, genre, price, pages) values (4, 'Not Mujs Book2', 'Not Muj', 1004, 'Comedy', 23, 234);
                    INSERT INTO Book (bookID, bookName, authorName, ISBN, genre, price, pages) values (3, 'LOLGuide', 'xd', 1003, 'Fictional', 50, 93);

                    INSERT INTO Author (AuthID, AuthName) values (51, 'Mujtaba');
                    INSERT INTO Author (AuthID, AuthName) values (52, 'Not Muj');

                    INSERT INTO Users (UserID, UserName, BillingInfo, ShippingInfo, PhoneNum) values (61, 'Shrek', '1435 King St.', '1435 King St.', 613222222);
                    INSERT INTO Users (UserID, UserName, BillingInfo, ShippingInfo, PhoneNum) values (62, 'Jett', '1433 King St.', '1433 King St.', 613222332);

                    INSERT INTO CheckoutBasket (CartID, bookName, bookQuantity, totalPrice, billingInfo, shippingInfo) values (501, 'Mujtabas Book1', 1, 10, '1435 King St.', '1435 King St.');
                    INSERT INTO CheckoutBasket (CartID, bookName, bookQuantity, totalPrice, billingInfo, shippingInfo) values (502, 'Not Mujs Book1', 2, 40, '1433 King St.', '1433 King St.');

                    INSERT INTO Orders (OrderNumber, userName, userID, ShipmentDate) values (1, 'Shrek', 61, '2022-05-10');
                    INSERT INTO Orders (OrderNumber, userName, userID, ShipmentDate) values (2, 'Jett', 62, '2023-01-12');

                    INSERT INTO Report (ReportID, TotalSales, TotalExpenditure, SalesperGenre, SalesperAuthor) values (5, 2, 25, 2, 2);

                    INSERT INTO Owner (OwnID, OwnerEmail, OwnerPhone, OwnerName, BankAccount) values (9000, 'gg@valorant.com', 423122, 'John', 12312);

                    
                    INSERT INTO Publisher (PubID, PubName, Address, Email, PhoneNumbers, BankingAccount) values (123, 'Louis', '213 Queens st.', 'lou@gmail.com', 132123, 2342432);
                    INSERT INTO Publisher (PubID, PubName, Address, Email, PhoneNumbers, BankingAccount) values (124, 'Nang', '23 Ls st.', 'nha@gmail.com', 1321312123, 234322);

                    INSERT INTO search (bookID, UserID) values (1, 61);
                    INSERT INTO search (bookID, UserID) values (2, 62);

                    INSERT INTO addBook (bookID, CartID) values (1, 501);
                    INSERT INTO addBook (bookID, CartID) values (2, 502);

                    INSERT INTO written (bookID, AuthID) values (1, 51);
                    INSERT INTO written (bookID, AuthID) values (2, 52);

                    INSERT INTO published (bookID, PubID) values (1, 123);
                    INSERT INTO published (bookID, PubID) values (2 ,124);

                    INSERT INTO register (CartID, UserID) values (501, 61);
                    INSERT INTO register (CartID, UserID) values (502, 62);

                    INSERT INTO placeOrder (CartID, OrderNumber) values (501, 1);
                    INSERT INTO placeOrder (CartID, OrderNumber) values (502, 2);

                    INSERT INTO track (UserID, OrderNumber) values (61, 1);
                    INSERT INTO track (UserID, OrderNumber) values (62, 2);

                    INSERT INTO ship (UserID, OrderNumber, shippingCompany) values (61, 1, 'FedUP');
                    INSERT INTO ship (UserID, OrderNumber, shippingCompany) values (62, 2, 'DOWNS');

                    INSERT INTO transfer (PubID, OrderNumber) values (123, 1);
                    INSERT INTO transfer (PubID, OrderNumber) values (124, 2);

                    INSERT INTO recordSale (ReportID, OrderNumber) values (5, 1);
                    INSERT INTO recordSale (ReportID, OrderNumber) values (5, 2);

                    INSERT INTO gets (ReportID, OwnID) values (5, 9000);

                    INSERT INTO adds (bookID, OwnID) values (3, 9000);
                    
                    INSERT INTO remove (bookID, OwnID) values (2, 9000);

                    INSERT INTO sendEmail (PubID, OwnID) values (123, 9000); '''
    #these are to run the ddl statemnents above so
    #they are executed and the results are shown on pgAdmin4
    cur.execute(dropTables)
    cur.execute(createTables)
    cur.execute(insertTables)
    connect.commit()

    print("This is a text based UI, to interact with the BookStore UI you need to provide some input. ")
    userInp = input("Would you like to run as a: 1) user 2) owner 3) quit? ").lower()
    #While loop doesn't exit until user specifies it.
    while(userInp != "quit"):
        #Operator has the option to run the program as user or owner.
        if(userInp == "user"):
            print(userInp)
            #to see if the user wants to see a book, buy a book, or track an existing order.
            option = input("What would you like to do: 1) see 2) buy 3) track,  a book/order?  ").lower()
            #these are all the options to view a book by:
            #user can search for it by bookname, authorname, isbn, genre
            if(option == "see"):
                search = input("How would you like to search for the book by \n 1) bookname. \n 2) AuthorName \n 3) ISBN \n 4) genre ? ").lower()
                if(search == "bookname"):
                    inp = input("Enter BookName, has to be be in the same format as it is in the Database. ")
                    insert = "SELECT * FROM Book WHERE bookName='"+ inp +"';"
                    cur.execute(insert)
                    output = cur.fetchall()
                    for x in output:
                        print("Book ID: ", str(x[0]))
                        print("Book Name: ", x[1])
                        print("Author Name: ", x[2])
                        print("ISBN: ", str(x[3]))
                        print("Genre: ", x[4])
                        print("Price: $", str(x[5]))
                        print("Number of Pages: ", str(x[6]))

                elif(search == "authorname"):
                    inp = input("Enter AuthorName, has to be be in the same format as it is in the Database. ")
                    insert = "SELECT * FROM Book WHERE authorName='"+ inp +"';"
                    cur.execute(insert)
                    output = cur.fetchall()
                    for x in output:
                        print("Book ID: ", str(x[0]))
                        print("Book Name: ", x[1])
                        print("Author Name: ", x[2])
                        print("ISBN: ", str(x[3]))
                        print("Genre: ", x[4])
                        print("Price: $", str(x[5]))
                        print("Number of Pages: ", str(x[6]))

                elif(search == "isbn"):
                    inp = input("Enter ISBN, has to be be in the same format as it is in the Database. ")
                    insert = "SELECT * FROM Book WHERE ISBN='"+ inp +"';"
                    cur.execute(insert)
                    output = cur.fetchall()
                    for x in output:
                        print("Book ID: ", str(x[0]))
                        print("Book Name: ", x[1])
                        print("Author Name: ", x[2])
                        print("ISBN: ", str(x[3]))
                        print("Genre: ", x[4])
                        print("Price: $", str(x[5]))
                        print("Number of Pages: ", str(x[6]))

                elif(search == "genre"):
                    inp = input("Enter Genre to be be in the same format as it is in the Database. ")
                    insert = "SELECT * FROM Book WHERE genre='"+ inp +"';"
                    cur.execute(insert)
                    output = cur.fetchall()
                    for x in output:
                        print("Book ID: ", str(x[0]))
                        print("Book Name: ", x[1])
                        print("Author Name: ", x[2])
                        print("ISBN: ", str(x[3]))
                        print("Genre: ", x[4])
                        print("Price: $", str(x[5]))
                        print("Number of Pages: ", str(x[6]))

            #if the user chooses to buy, they have to enter a valid book name.
            elif(option == "buy"):
                search= input("Enter the name of the book you would like to buy? ")
                cart =  int(input("Enter your cartID? Please type your existing cartID, or make a new cart"))
                quan = int(input("Enter the quantity you want to buy? "))

                sel = "SELECT * FROM Book WHERE bookName='"+ search +"';"
                cur.execute(sel)
                output = cur.fetchall()
                name = ""
                price = 0

                for r in output:
                    print(r[1], r[5])
                    name = r[1]
                    price = r[5]

                price *= quan

                billingAdd = input("Enter the billing Address? ")
                shippingAdd = input("Enter the shipping Address? ")
                
                ins = "INSERT INTO CheckoutBasket (CartID, bookName, bookQuantity, totalPrice, billingInfo, shippingInfo) VALUES (%s, '"+ name +"', %s, %s, '"+ billingAdd +"', '"+ shippingAdd +"');"
                insertInts = (cart, quan, price)
                cur.execute(ins, insertInts)
                connect.commit()

            #if the user wishes to track an order, they have to enter a valid order number.
            elif(option == "track"):
                ord= input("Enter the order number to track i? ")
                ins = "SELECT * FROM Orders WHERE OrderNumber='"+ ord +"';"
                cur.execute(ins)
                output = cur.fetchall()
                for x in output:
                    print("Order Number: ", str(x[0]))
                    print("Placed by UserName: ", x[1])
                    print("Placed by UserID: ", str(x[2]))
                    print("Expected Shipment Date: ", str(x[3]))

        #this is if the operator runs it as an owner.
        elif(userInp == "owner"):
            print("You're the owner of the store!")
            option = input("What would you like to do: 1) Add 2) Remove 3) Report,  a book/order?  ").lower()
            #add a book to the bookstore
            if(option == "add"):
                id= int(input("Enter the ID of the book? "))
                name = input("Enter the name of the book? ")
                authName = input("Enter the author of the book? ")
                isbn= int(input("Enter the ISBN number of the book? "))
                genre = input("Enter the genre of this book? ")
                price= int(input("Enter the price of the book? "))
                page= int(input("Enter the number of pages of this book? "))
                ins = "INSERT INTO Book (bookID, bookname, authorName,ISBN, genre, price, pages) VALUES (%s, '"+ name +"', '"+ authName +"', %s, '"+ genre +"', %s, %s);"
                details = (id, isbn, price, page)
                cur.execute(ins, details)
                connect.commit()



                

            #remove a book from the bookstore.
            elif(option == "remove"):
                rem = input("Enter the book ID you want to remove? ")
                delt = "DELETE FROM remove WHERE bookID = '"+ rem +"';"
                cur.execute(delt)
                connect.commit()

            
            #display reports of all the sales.
            elif(option == "report"):
                repo = input("Enter the ID of the report you want? ")
                sell = "SELECT * FROM Report WHERE ReportID = '" + repo + "';"
                cur.execute(sell)
                output = cur.fetchall()
                for x in output:
                    print("Report ID : ", str(x[0]))
                    print("Total Sales: ", str(x[1]))
                    print("Total Expenditure: ", str(x[2]))
                    print("Sales Per Author: ", str(x[3]))
                    print("Sales Per Genre: ", str(x[4]))
        else:
            print("Invalid Input, please describe if you are the owner or user.")

        userInp = input("Would you like to run as a: 1) user 2) owner? ").lower()

    print("Program shut down... .. .")

#if there is an error conncecting with postgreSQL, this error is thrown.
except Exception as error:
    print("ERROR! Could not connect to postgreSQL, might be invalid password or something else.", error)

#when the script is ran, this ends the connection with the database.
finally:
    if(connect):
        cur.close()
        connect.close()
        print("Connection closed to PostgreSQL")