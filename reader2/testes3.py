class create_passenger():
    def __init__ (self):
        self.passenger = 'lucas222'
        self.seat = 27
        self.flight_number = 555
        self.aircraft = 'taca fire'


    def card_printer(self):
        output= "name: {0}" '\n' "flight: {1}" '\n' "seat: {2}" '\n'"aircraft: {3}" '\n'  "|".format(self.passenger, self.flight_number, self.seat, self.aircraft)
        banner = '+' + '-' * (len(output) -2)+ '+'
        border = 'l' + '' * (len(output) -2) + 'l'
        lines = [banner, border, output, border, banner]
        card = '\n'.join(lines)
        print(card)
        print()

c1 = create_passenger()

c1.card_printer()


def test1(passenger, seat, flight_number, aircraft):
    passenger = 'lucas'
    seat = 27
    flight_number = 555
    aircraft = 'taca fire'
    output= "name: {0}" \
            "flight {1}" \
            "seat {2}" \
            "aircraft {3}" \
                .format(passenger, flight_number, seat, aircraft)
    return output