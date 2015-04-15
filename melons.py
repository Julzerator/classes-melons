"""This file should have our melon-type classes in it."""

class Melon(object):
    
    def get_base_price(self):

        return 5



class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']


    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty   # getting the base total times qty
        if qty >= 3:
            total = total * .75 # if the customer orders 3 or more, discount 75%

        return total


class CantaloupeOrder(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given number of Cantaloupe ordered."""

        total = self.get_base_price() * qty
        if qty >= 5:
            total = total * .5 # if the customer orders 5 or more, discount 50%

        return total

class CasabaOrder(Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons  = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of Casaba ordered."""

        total = (self.get_base_price() + 1) * qty # Casaba base cost is $1 more.
        total = total  * 1.5  # imported is 1.5 times the total

        return total


class SharlynOrder(Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons  = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of Sharlyn ordered."""

        total = self.get_base_price() * qty
        total = total  * 1.5  # imported is 1.5 times the total

        return total


class SantaClauseOrder(Melon):
    species = "Santa Clause"
    color = "green"
    imported = True
    shape = "natural"
    seasons  = ['Spring', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of Santa Clause ordered."""

        total = self.get_base_price() * qty
        total = total  * 1.5  # imported is 1.5 times the total

        return total


class ChristmasOrder (Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons  = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of Christmas ordered."""

        total = self.get_base_price() * qty

        return total


class HornedMelonOrder(Melon):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons  = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of Horned Melon ordered."""

        total = self.get_base_price() * qty
        total = total  * 1.5  # imported is 1.5 times the total

        return total


class XinguaOrder(Melon):
    species = "Xingua"
    color = "black"
    imported = True
    shape = "square"
    seasons  = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of Xingua ordered."""

        total = self.get_base_price() * qty  # getting the base total times qty
        total = total * 1.5 # imported is 1.5 times the total
        total = total * 2 # square cost 2 times 


        return total

class OgenOrder(Melon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons  = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of Ogen ordered."""

        total = (self.get_base_price() + 1) * qty # Ogen base cost is $1 more.
        total = total  * 1.5  # imported is 1.5 times the total

        return total