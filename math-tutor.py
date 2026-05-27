print('Project -  Math Tutor')

num_ques = int(input("How many practice questions do you want?: "))

highest_num = 9

while True: 
    highest_num = int(input("How high do you want the multiplication numbers to be?: "))
    if highest_num > 12: 
        print("The number can't go over 12! Try again.")
        continue
    else: 
        break

total_correct = 0

from random import randrange 

all_ques = []
all_ans = []
cor_ans = []

import time

all_res_time = []

for i in range (num_ques):
    num1, num2 = randrange (1,highest_num), randrange (1,highest_num)
    ans = num1 * num2

    start_time = time.time()
    question = int(input( f'{num1} x {num2} = '))
    end_time = time.time()

    response_time = end_time - start_time
    all_res_time.append(response_time)

    if question == ans:
        total_correct += 1
    
    all_ques.append(f'{num1} x {num2}')
    all_ans.append(question)
    cor_ans.append(f'{ans}')

print("==== RESULT ====")
print(f'Thank you for playing! \n Correct answers = {total_correct}/{num_ques}\n You got {(total_correct/num_ques * 100):.0f}% correct!')
print(f'It took you {sum(all_res_time):.0f} seconds to complete the quiz. \n (Average time spent per question: {round(sum(all_res_time)/num_ques)})')
print(f'See all the questions below: ')
for i in range(len(all_ques)):
    print (f'Question {i+1}. {all_ques[i]} \n Your answer = {all_ans[i]} (Correct answer = {cor_ans[i]}) \n Time spent: {all_res_time[i]:.2f}s')


