from unittest import TestCase
from tkinter import *
import math
class Testcalc( TestCase ) :
    def test_swap( self) :
        root = Tk( )
        self.e = Entry( root )
        EndVaule = 0
        self.e.insert( 0, EndVaule )
        e = self.e.get( )
        EndVaule = "x"
        self.e.insert( 0, EndVaule )
        EndVaule = 2
        self.e.insert( 0, EndVaule )
        e = self.e.get( )
        print( e )
        self.expression = self.e.get( )
        self.newtext = self.expression.replace( 'x', '*' )
        print(self.newtext)
        if( self.newtext =="2*0"):
            print("Ok")
        else:self.fail( )

    def test_equals( self ) :

        root = Tk( )
        self.newtext = "2+0"
        self.e = Entry( root )
        EndVaule = 0
        self.e.insert( 0, EndVaule )
        e = self.e.get( )
        EndVaule = "+"
        self.e.insert( 0, EndVaule )
        EndVaule = 2
        self.e.insert( 0, EndVaule )
        e = self.e.get( )
        print(e)

        try :
            # evaluate the expression using the eval function
            self.value = eval( self.newtext )
            print( self.value )
        except ZeroDivisionError :
            self.e.delete( 0, END )
            self.e.insert( 0, 'Error' )
        except SyntaxError or NameError :
            self.e.delete( 0, END )
            self.e.insert( 0, 'Error' )
        else :
            if self.value > 999999999999999999 :
                self.e.delete( 0, END )
                self.e.insert( 0, 'Error' )
            else :

                self.e.delete( 0, END )
                self.e.insert( 0, self.value )
    def test_equals2( self ) :
        """when the equal button is pressed"""
        root = Tk( )
        self.newtext = "2/0"
        self.e = Entry( root )
        EndVaule = 0
        self.e.insert( 0, EndVaule )
        e = self.e.get( )
        EndVaule = "/"
        self.e.insert( 0, EndVaule )
        EndVaule = 2
        self.e.insert( 0, EndVaule )
        e = self.e.get( )
        print(e)


        try :
            # evaluate the expression using the eval function
            self.value = eval( self.newtext )
            print( self.value )
        except ZeroDivisionError :
            self.e.delete( 0, END )
            self.e.insert( 0, 'Error' )
            print("Error")
        except SyntaxError or NameError :
            self.e.delete( 0, END )
            self.e.insert( 0, 'Error' )
        else :
            if self.value > 999999999999999999 :
                self.e.delete( 0, END )
                self.e.insert( 0, 'Error' )
            else :

                self.e.delete( 0, END )
                self.e.insert( 0, self.value )

    def test_clearall( self ) :
        root = Tk( )
        self.e = Entry(root )
        EndVaule=2
        self.e.insert( 0, EndVaule )
        e=self.e.get()
        print("wartosc  self.e przed clear:",e)
        self.e.delete( 0, END )
        e = self.e.get( )
        if e=="":
            print( "wartosc  self.e po clear:",e )
        else:
            self.fail( )
    def test_square( self ) :
        """square method"""
        root = Tk( )
        self.e = Entry( root )
        EndVaule = 2
        self.e.insert( 0, EndVaule )
        e = self.e.get( )
        self.newtext = "2"
        print( "wartosc  self.e przed squere:", e )

        try :
            self.value = eval( self.newtext )

        except SyntaxError or NameError :
            self.e.delete( 0, END )
            self.e.insert( 0, 'Error' )
        else :
            if self.value > 999999999999999999 :
                self.e.delete( 0, END )
                self.e.insert( 0, 'Error' )
            else :
                self.sqval = math.pow( self.value, 2 )
                if self.sqval > 999999999999999999 :
                    print( self.sqval )
                    self.e.delete( 0, END )
                    self.e.insert( 0, 'Error' )
                else :
                    print( self.sqval )
                    self.e.delete( 0, END )
                    self.e.insert( 0, self.sqval )

    def test_action( self,EndVaule=2 ) :
        root = Tk( )
        self.e = Entry( root )
        e = self.e.get( )
        print("Wartość przed dodaniem:",e)
        self.e.insert( END, EndVaule )
        e = self.e.get( )
        if e == "2":
            print("wartość po dodaniu:",e)
        else:

            self.fail( )
