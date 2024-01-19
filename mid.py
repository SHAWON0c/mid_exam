class Hall:
    def __init__(self,rows,coll,hall_no) -> None:
        self._seats={}
        self._show_list=[]
        self._rows=rows
        self._coll=coll
        self._hall_no=hall_no
    
    
    def book_seats(self,id,list):
        if id in self._seats:
            seats=self._seats[id]
            for seat in list:
                rows,col=seat
                if 0<=rows<self._rows and 0<=col< self._coll:
                    if seats[rows][col]==0:
                        seats[rows][col]=1
                        print(f'Seat ({rows},{col}) is Booked ')
                    else:
                        print(f'Seat ({rows},{col}) is Already Booked')
                else:
                    print(f'invalid Seat ({rows},{col})')
        else:
            print(f'Invalid ID , Movie ID-{id} Not Found')

    def Show_Entry(self,id,movie_name,time):
        info=(id, movie_name, time)
        self._show_list.append(info)

        seat=[]
        for i in range(self._rows):  
            rows=[]
            for j in range(self._coll):
                rows.append(0)
            seat.append(rows)
        self._seats[id]=seat


    
    def view_show_list(self):
        print(f'\nHALL NO-{self._hall_no} All Running Show')
        print('--------------------------------------------')
        for show in self._show_list:
            print(show)
    
    def view_available_seats(self, id):
     if id not in self._seats:
        print("Invalid ID. Please provide a valid ID.")
        return
     print(f'Available seats for Movie ID {id}:')
     seat = self._seats[id]
     for ache in seat :
         print(ache)
    

""" def view_available_seats(self,id):
        print(f' available seats:')
        
        seat=self._seats[id]
        for ache in seat:
            print(ache) """

class Star_Cinema:
    _hall_list=[]

    def Hall_entry(self,hall):
        self._hall_list.append(hall)
    

ob1=Hall(6,6,1)
chinema=Star_Cinema()
chinema.Hall_entry(ob1)

ob1.Show_Entry('111','12TH FAIL(111)','3:00 PM BD-Time , 2024')
ob1.Show_Entry('222','KING OF KATHA(222)','8:00 PM BD-Time , 2024')



while True:
    print('\n1. VIEW ALL RUNNING SHOW TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4.EXIT')
    op =int(input('ENTER YOUR OPTION: '))

    if op==1:
        ob1.view_show_list()

    elif op==2:
        d=input('MOVIE ID : ')
        ob1.view_available_seats(d)

    elif op==3:
        a=input('MOVIE ID : ')
        b=int(input('Number of Ticket: '))

        list_all=[]

        for i in range(0,b):
            d=int(input('Enter ROW: '))
            c=int(input('Enter COLUMN: '))
            list_all.append((d,c))
        ob1.book_seats(a,list_all)

    elif op==4:
        break