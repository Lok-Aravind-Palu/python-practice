from pprint import pprint as pp


class ThisClass:

    def calc_func(self,num1,num2):
        return num1+num2

    def print_calcu(self,res):
        print(res)

    def givenum(self):
        self.print_calcu(self.calc_func(30,70))



x = ThisClass()
x.givenum()

print("-----------------------------------------------------------------------------------------------------")

# Flight Example

class Flight:

    def __init__(self,number,aircraft):

        if not number[:2].isalpha():
            raise ValueError("No airline number {}".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline number {}".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number ()".format(number))


        self._number = number
        self._aircraft = aircraft
        rows, seats =self._aircraft.aircraft_seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]



    def number(self):
        return self._number

    def airplane(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.aircraft_model()

    def _parse_seat(self, seat):

        row_numbers,seat_letters = self._aircraft.aircraft_seating_plan()


        letter = seat[1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))


        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))

        return row,letter



    def allocate_seats(self, seat, passenger):


        row,letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger


    def relocate_passenger(self,from_seat,to_seat):


        from_row,from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to allocate in seat {}".format(from_seat))


        to_row,to_letter =self._parse_seat(to_seat)
        if self._seating[to_row][to_seat] is not None:
            raise ValueError("Seat {} already Occupied ".format(to_seat))

        self._seating[to_row][to_seat] = self._seating[from_row][from_seat]
        self._seating[from_row][from_seat] = None

    def num_available_Seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                       for row in self._seating
                        if row is not None)



class Aircrafght:

    def __init__(self,model,registration,num_rows,num_seats_per_rows):
        self._model = model
        self._registration = registration
        self._num_rows = num_rows
        self._num_seats_per_rows = num_seats_per_rows



    def aircraft_model(self):
        return self._model


    def aircraft_registration(self):
        return self._registration

    def aircraft_num_rows(self):
        return self._num_rows

    def aircraft_num_seats_per_rows(self):
        return self._num_seats_per_rows

    def aircraft_seating_plan(self):
        return (range(1,self._num_rows+1),"ABCDEFGHJK"[:self._num_seats_per_rows])


    def make_flight(self):
        flig = Flight("BA739", Aircrafght("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_rows=6))
        # print(flig.aircraft_model())
        # print(flig._seating)
        # pp(flig._seating)
        #
        # pp(flig.allocate_seats("12A", "Guido Van Rossum"))
        # # pp(flig.allocate_seats("12A","Rasmus Ledorf"))
        #
        # pp(flig.allocate_seats("15F", "Baijan Stroustrup"))
        # pp(flig.allocate_seats("15E", "Anders Hejelberg"))
        # # pp(flig.allocate_seats("E27","Mukihiro Matusumo"))
        #
        # pp(flig.allocate_seats("1C", "John MacCarthy"))
        # pp(flig.allocate_seats("1D", "Richard Hickey"))
        # # pp(flig.allocate_seats("DD","Lary well"))
        #
        # pp(flig._seating)

        flig.allocate_seats("12A", "Guido Van Rossum")
        flig.allocate_seats("15F", "Baijan Stroustrup")
        flig.allocate_seats("15E", "Anders Hejelberg")
        flig.allocate_seats("1C", "John MacCarthy")
        flig.allocate_seats("1D", "Richard Hickey")
        return flig


f = Aircrafght("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_rows=6).make_flight()

f.relocate_passenger("12A","15D")
pp(f._seating)
pp(f.num_available_Seats())