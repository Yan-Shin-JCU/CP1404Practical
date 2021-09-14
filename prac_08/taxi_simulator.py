from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

current_taxi = None
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
chosen_taxis = []
bill = 0
print("Let's drive!")


while current_taxi is None:
    user_choice = input('q)uit, c)hoose taxi, d)rive\n>>> ')
    print('Bill to date: ${:.2f}'.format(bill))
    print('Invalid option')
    user_choice = input('q)uit, c)hoose taxi, d)rive\n>>> ')

    if user_choice == 'c':
        count = 0
        for taxi in taxis:
            print('{} - {}'.format(count, taxi))
            count += 1
        try:
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice > len(taxis):
                print('Invalid taxi choice')

        except ValueError:
            print('Invalid taxi choice')

    elif user_choice == 'd':
        drive_distance = input('Drive how far? ')
        taxis[0].drive(drive_distance)
        travel_cost = taxis[0].get_fare()
        bill += travel_cost
        print('Your trip cost you ${:.2f}'.format(taxis[0]))


