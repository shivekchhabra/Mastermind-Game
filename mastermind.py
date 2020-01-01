# Mastermind Game
import numpy as np


def instructions():
    z = np.arange(10)
    print(
        '\n\nThe aim of the game is to decode the number pattern as selected by CPU or the other player.\n For every digit, the player shall get 3x chances.\n For example, if the number of digits is set to 3, there will be 9 chances to decode the number combination.\n\nIf the number is correct and at the right location, it will be marked in right answers,\n else if the number is not right or at an incorrect location, it will be marked in wrong answers\n Choose numbers between:\n',
        z)


def mode_selection():
    instructions()
    x = input('Single player(s) or multiplayer(m): ')
    num_comb = int(input('\n\nEnter the number of combination of digits (less than 9): '))
    tries = 3 * num_comb - 1

    print('\n GoodLuck!')
    if x == 's':
        ans = 0 + (9 - 0) * np.random.random(num_comb)
        ans = ans.round()

    else:
        ans = np.zeros([num_comb])
        print('\n enter the answer combination')
        for i in range(num_comb):
            print('value: ', i + 1)
            ans[i] = int(input())
    return ans, tries, num_comb


def game_play():
    ans, tries, num_comb = mode_selection()
    print(
        '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    counter = 0
    while (counter <= tries):
        flag = 0
        counter = counter + 1
        user_ans = np.zeros([num_comb])
        c1 = 0
        c3 = 0
        print('\n Enter numbers')

        print('\nchance: ', counter)
        for j in range(num_comb):
            temp = int(input('value: '))
            user_ans[j] = temp

        for k in range(num_comb):

            if user_ans[k] == ans[k]:
                c1 = c1 + 1

            else:
                c3 = c3 + 1

        print('\n\n', 'number of right answers', c1, '\n', 'number of wrong answers', c3)

        for i in range(num_comb):
            if ans[i] == user_ans[i]:
                flag = flag + 1
        if flag == num_comb:
            print('\n\nCongratulations you win!!!\n\n')
            counter = tries + 10

    if counter == tries + 1:
        print('\n\nSorry please try again')
        print('The answer was: ', ans)


if __name__ == '__main__':
    game_play()
