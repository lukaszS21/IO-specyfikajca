from tkinter import *
import math

max=999999999999999999
# klasa calc
class calc :
    '''zamiana znaków'''
    def Swap( self ) :

        self.expression = self.e.get( )
        self.newtext = self.expression.replace( 'x', '*' )
    def equals( self ) :
        self.Swap( )
        try :
            self.value = eval( self.newtext )

        except ZeroDivisionError :
            self.e.delete( 0, END )
            self.e.insert( 0, 'Error' )
        except SyntaxError or NameError :
            self.e.delete( 0, END )
            self.e.insert( 0, 'Error' )
        else :
            if self.value > max :
                self.e.delete( 0, END )
                self.e.insert( 0, 'Error' )
            else :
                self.e.delete( 0, END )
                self.e.insert( 0, self.value )

    def clearall( self ) :
        self.e.delete( 0, END )

    def square( self ) :
        self.Swap( )
        try :
            self.value = eval( self.newtext )


        except SyntaxError or NameError :
            self.e.delete( 0, END )
            self.e.insert( 0, 'Error' )
        else :
            if self.value > max :
                self.e.delete( 0, END )
                self.e.insert( 0, 'Error' )
            else :
                self.sqval = math.pow( self.value, 2 )
                if self.sqval>max:
                    print( self.sqval )
                    self.e.delete( 0, END )
                    self.e.insert( 0, 'Error' )
                else:
                    print(self.sqval)
                    self.e.delete( 0, END )
                    self.e.insert( 0, self.sqval )

    def action( self, EndVaule ) :
        self.e.insert( END, EndVaule )



    def __init__( self, master ) :
        """Constructor method"""
        mycolor = '#%02x%02x%02x' % (64, 204, 208)
        master.title( 'Calulator' )
        master.geometry( )
        self.e = Entry( master )
        self.e.grid( row = 0, column = 0, columnspan = 6, pady = 3 )
        self.e.focus_set()



        Button( master, text = "=", width = 8, height = 3, fg = 'black',
                bg = mycolor, command = lambda : self.equals( ) ).grid(
            row = 5, column = 2 )

        Button( master, text = 'Clear', width = 8, height = 3,
                fg = 'black', bg = mycolor,
                command = lambda : self.clearall( ) ).grid( row = 5, column = 1 )

        Button( master, text = "+", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( '+' ) ).grid( row = 2, column = 3 )

        Button( master, text = "x", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( 'x' ) ).grid( row = 4, column = 3 )

        Button( master, text = "-", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( '-' ) ).grid( row = 3, column = 3 )

        Button( master, text = "/", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( '/' ) ).grid( row = 5, column = 3 )

        Button( master, text = "x²", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.square()).grid( row = 6, column = 1 )

        Button( master, text = "7", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( '7' ) ).grid( row = 4, column = 0 )

        Button( master, text = "8", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( 8 ) ).grid( row = 4, column = 1 )

        Button( master, text = "9", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( 9 ) ).grid( row = 4, column = 2 )

        Button( master, text = "4", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( 4 ) ).grid( row = 3, column = 0 )

        Button( master, text = "5", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( 5 ) ).grid( row = 3, column = 1 )

        Button( master, text = "6", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( 6 ) ).grid( row = 3, column = 2 )

        Button( master, text = "1", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( 1 ) ).grid( row = 2, column = 0 )

        Button( master, text = "2", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( 2 ) ).grid( row = 2, column = 1 )

        Button( master, text = "3", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( 3 ) ).grid( row = 2, column = 2 )

        Button( master, text = "0", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( 0 ) ).grid( row = 5, column = 0 )

        Button( master, text = ".", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( '.' ) ).grid( row = 6, column = 0 )

        Button( master, text = "(", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( '(' ) ).grid( row = 6, column = 2 )

        Button( master, text = ")", width = 8, height = 3,
                fg = "black", bg = mycolor,
                command = lambda : self.action( ')' ) ).grid( row = 6, column = 3 )
