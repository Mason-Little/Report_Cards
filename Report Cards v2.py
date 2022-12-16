import random

class_numbers = input('Number of Kids: ')
# date = input("what is the data (month day, year): ")
date = 'December 16, 2022'


for i in range(int(class_numbers)):
    name = input("Name:")
    skill = input("what is there skills:")
    improvement = input("what can they improve on: ")
    level = input("what should they register in: ")

    greeting = [f'Well done swimming this set, {name}!',
                f'You swam that set like a pro, {name}!',
                f'Great effort swimming this set, {name}!',
                f'You really nailed that set, {name}!',
                f'Keep up the awesome work swimming this set, {name}!',
                f'You are making amazing progress swimming this set, {name}!',
                f'Fantastic job swimming this set, {name}!',
                f'Keep up the great work swimming this set, {name}!',
                f'Excellent job swimming this set, {name}!',
                f'Superb work swimming this set, {name}!',
                f'You did an incredible job swimming this set, {name}!']

    skill_in_sentence = [f'Your {skill} is looking really good!',
                         f'Your {skill} is looking great!',
                         f'Your {skill} is looking awesome.',
                         f'Your {skill} has gotton so much better over this set.',
                         f'Your {skill} has improved so much over this short time with you.',
                         f'Your {skill} is really impressive!',
                         f'Your {skill} has come a long way!',
                         f'Your {skill} is getting stronger every day!',
                         f'Your {skill} is getting better and better!',
                         f'Your {skill} is looking fantastic!',
                         f'Your {skill} is truly impressive!']

    improvement_templates = [f'Next time try and {improvement}.',
                             f'Remember to always {improvement}.',
                             f'Just remember to {improvement}.',
                             f'Make sure to focus on {improvement} during your next lesson.',
                             f"Try to {improvement} when you're practicing your strokes.",
                             f'Remember to keep your {improvement} in mind as you swim.',
                             f'Try to work on {improvement} in your next set to improve your technique.',
                             f'Focus on {improvement} during your next set.']

    send_off = [f'Hope to see you again soon!']

    full = f"{random.choice(greeting)} {random.choice(skill_in_sentence)} {random.choice(improvement_templates)} {random.choice(send_off)}\nInstructor: Mason\nDate: {date}\nRegister in: Swimmer {level}\n\n"

    print(full)

    with open('Output.txt', 'a') as f:
        f.write(full)
