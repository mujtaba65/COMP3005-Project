
--THESE ARE ALL THE QUERIES TO DROP THE TABLES IF THEY EXIST
DROP TABLE IF EXISTS Book CASCADE;
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
    

--THESE ARE ALL THE QUERIES TO CREATE ALL THE TABLES.
CREATE TABLE IF NOT EXISTS Book(
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
);

--THESE ARE ALL THE QUERIES OF ENTERING DATA INTO THE TABLE
INSERT INTO Book (bookID, bookName, authorName,ISBN, genre, price, pages) values (1, 'Mujtabas Book1', 'Mujtaba' ,1001, 'Scary', 10, 423);
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

INSERT INTO sendEmail (PubID, OwnID) values (123, 9000); 