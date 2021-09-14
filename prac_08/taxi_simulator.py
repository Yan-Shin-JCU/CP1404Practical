from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

current_taxi = None
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
bill = 0
print("Let's drive!")


user_choice = input('q)uit, c)hoose taxi, d)rive\n>>> ')
while user_choice != 'c':
    print('Bill to date: ${:.2f}'.format(bill))
    print('Invalid option')
    user_choice = input('q)uit, c)hoose taxi, d)rive\n>>> ')

if user_choice == 'c':
    count = 0
    for taxi in taxis:
        print('{} - {}'.format(count, taxi))
        count += 1
    try:
        while current_taxi is None:
            taxi_choice = input("Choose taxi: ")
            if taxi_choice > len(taxis):
                print('Invalid taxi choice')
    except:
            print('Invalid taxi choice')


