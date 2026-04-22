      #databasesdifjn
books = []
Issued_books = []
#add function
def add_book():
    name= input('Enter the book name')
    books.append(name)
    print(name,'is added successfully')
def show_books():
    if len(books)==0:
        print('No books available')
    else:
        print('Available books')
        for b in books:
            print(b)
def issue_book():
    if len(books)==0:
        print('No books available')
        return
    else:
        show_books()
        name= input('Enter the book name you want to issue')
        if name in books:
            Issued_books.append(name)
            books.remove(name)
            print (name, 'is issued')
        else:
            print(name,'is not available')
def return_book():
    name= input('Enter the book name you want to return:')
    if name in Issued_books:
        Issued_books.remove(name)
        books.append(name)
        print(name,'book returned')
    else:
        print(name,'book was never issued')
def library ():
    while True:
        print('1. Menu')
        print('2. Add book')
        print('3. Show books')
        print('4. Issue Book')
        print('5. Return Book')
        print('6. Exit')
        
Choice = int(input('Enter your choice:'))
if Choice == 1:
    add_book()
elif Choice == 2:
    show_books()
elif Choice == 3:
    issue_book()
elif Choice == 4:
    return_book()
elif Choice == 5:
    print('Thank You')
    "break"
