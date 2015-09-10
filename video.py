import math
import random
class Customer(object):
    def __init__(self):
        self.name=raw_input("Customer's name: ")
        self.id_no=raw_input("Customer's id number: ")
        self.points=0
        self.charge=0
        self.borrowed=[]
        self.discount=0

    """Customer object borrows books"""
    def borrow(self):
                while True:
                        choice=raw_input("Does the customer wish to borrow a movie? \n1. Yes\n2.No\nChoice:")
                        if choice =='1':
                                self.borrowed.append(Movie())
                        else:
                                break
                while True:
                    self.days_borrowed=raw_input("Number of days to be borrowed: ")
                    if self.days_borrowed.isdigit():
                            break 
                    else:
                            print "Please enter a digit"

    """Customer object earns points""" 
    def earn_points(self):
            if [(movie.category) for movie in self.borrowed].count("New release")>1:
                                 self.points=1
            else:
                                 pass

    """Customer object returns movie borrowed"""
    def return_movies(self):
            self.discount=0
            late_movies=[]
            for movie in self.borrowed:
                    print movie.id, '. ', movie.title, "==>", movie.price
            while True:
                    late=raw_input("Enter code for movie returned late, press any letter to exist: ")
                    if late.isdigit():
                            if int(late) in [(movie.id) for movie in self.borrowed]: 
                                    for movie in self.borrowed:
                                            if movie.id==int(late):
                                                    self.borrowed.remove(movie)
                                                    late_movies.append(movie)
                                            else:
                                                continue
                            else: 
                                    print "Code doesnt exist"
                    else: 
                            break
            while True:
                    extra=raw_input("Extra days: ")
                    if extra.isdigit():
                            break
                    else:
                            print "Please enter a digit"
            print "Customer name: %s\nNumber of days: %s\nMovie name\tCategory\t\tPrice"%(self.name, extra)
            for movie in late_movies:
                    print "%s\t\t%s\t%d"%(movie.title, movie.category, movie.price*int(extra))
            self.charge=sum([(movie.price) for movie in late_movies])*int(extra)

            print "Discount: %d" %self.discount
            print "Total discounted charge: %d"%math.ceil(self.charge)

    
class Movie(object):
    def __init__(self):
        self.title=raw_input("Movie title: ")
        self.category=movie_category(self)
        self.id=random.randrange(1, 99)

"""Prompt for movie category"""
def movie_category(movie):
            cat=raw_input("1. Children's\n2. New release\n3. Regular\nEnter category for the movie[1-3]: ")
            if cat.isdigit():
                    if cat=='1':
                            movie.price=300
                            return "Children's"
                    elif cat == '2':
                            movie.price=1000
                            return "New release"
                    elif cat=='3':
                            movie.price=500
                            return "Regular"
                    else:
                            print "Please enter a choice between 1 and 3"
                            movie_category(movie)
            else:
                    print "Invalid input"
                    movie_category(movie)

                    
"""print customer receipt of borrowed movies"""
def print_borrowed(customer):
	print "Customer name: %s\nNumber of days: %s\nMovie name\tCategory\t\tPrice"%(customer.name, customer.days_borrowed)
	for movie in customer.borrowed:
		print "%s\t\t%s\t%d"%(movie.title, movie.category, movie.price*int(customer.days_borrowed))
	customer.earn_points()
	customer.charge=sum([(movie.price) for movie in customer.borrowed])*int(customer.days_borrowed)
	print "Total charge without discount: %d"%customer.charge
	if customer.points:
		customer.discount=customer.charge*0.1
		customer.charge-=customer.discount

	print "Discount: %d" %customer.discount
	print "Total discounted charge: %d"%math.ceil(customer.charge)



if __name__ == "__main__":
        print "Video library charges calculator"
        cus=Customer()
        cus.borrow()
        print_borrowed(cus)
        cus.return_movies()

