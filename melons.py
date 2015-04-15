"""This file should have our melon-type classes in it."""
BASE_COST = 5

class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = BASE_COST * qty   # getting the base total times qty
        if qty >= 3:
            total = total * .75 # if the customer orders 3 or more, discount 75%

        return total


class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given number of Cantaloupe ordered."""

        total = BASE_COST * qty
        if qty >= 5:
            total = total * .5 # if the customer orders 5 or more, discount 50%

        return total

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons  = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of Casaba ordered."""

        total = (BASE_COST + 1) * qty # Casaba base cost is $1 more.
        total = total  * 1.5  # imported is 1.5 times the total

        return total


class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons  = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of Sharlyn ordered."""

        total = BASE_COST * qty
        total = total  * 1.5  # imported is 1.5 times the total

        return total


class SantaClauseOrder(object):
    species = "Santa Clause"
    color = "green"
    imported = True
    shape = "natural"
    seasons  = ['Spring', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of Santa Clause ordered."""

        total = BASE_COST * qty
        total = total  * 1.5  # imported is 1.5 times the total

        return total


class ChristmasOrder (object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons  = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of Christmas ordered."""

        total = BASE_COST * qty

        return total


class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons  = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of Horned Melon ordered."""

        total = BASE_COST * qty
        total = total  * 1.5  # imported is 1.5 times the total

        return total


class XinguaOrder(object):
    species = "Xingua"
    color = "black"
    imported = True
    shape = "square"
    seasons  = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of Xingua ordered."""

        total = BASE_COST * qty  # getting the base total times qty
        total = total * 1.5 # imported is 1.5 times the total
        total = total * 2 # square cost 2 times 


        return total

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons  = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of Ogen ordered."""

        total = (BASE_COST + 1) * qty # Ogen base cost is $1 more.
        total = total  * 1.5  # imported is 1.5 times the total

        return total