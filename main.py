import random
class_amount = int(input("How many kids do you have in the class? "))

for i in range(class_amount):
    data = 'June 24, 2022'
    name = input(f"{i + 1} What is their name? ")
    GoodThing = input(f"{i + 1} What is a good thing about them? ")
    improvement = input(f"{i + 1} What is a thing they should be improving on? ")
    current_level = input(f"{i + 1} What is their current level? ")
    next_level = input(f"{i + 1} What is their next level? ")
    did_they_pass = input(f"{i + 1} Did they pass? ")

    greet = [f'Awesome work swimming this set {name}!',f'Great job swimming this set {name}!', f'Nice work swimming this set {name}!', f'Wonderful job swimming this set {name}!', f'Amazing work swimming this set {name}!']
    good_thing = [f'Your {GoodThing} is looking really good!', f'Your {GoodThing} is looking great!', f'Your {GoodThing} is looking awesome.',
                  f'Your {GoodThing} has gotton so much better over this set.', f'Your {GoodThing} has improved so much over this short time with you.']
    improvement_thing = [f'Next time try and {improvement}.', f'Remember to always {improvement}.', f'Just remember to {improvement}.']
    ending = 'Hope to see you again soon!'
    if did_they_pass == 'yes':
        #write to Output.txt
        with open('Output.txt', 'a') as f:
            f.write(f'{random.choice(greet)} {random.choice(good_thing)} {random.choice(improvement_thing)} {ending}\n')
            f.write('Instructor: Mason' + '\n')
            f.write('Date: ' + data + '\n')
            f.write(f"Register in: {next_level}" + '\n')
            f.write('\n')

    elif did_they_pass == 'no':
        with open('Output.txt', 'a') as f:
            f.write(f'{random.choice(greet)} {random.choice(good_thing)} {random.choice(improvement_thing)} {ending}\n')
            f.write('Instructor: Mason' + '\n')
            f.write('Date: ' + data + '\n')
            f.write(f"Register in: {current_level}" + '\n')
            f.write('\n')

    print()
    print('---------------------------------------------------------------------------------------------------------------------')
    print()

