low = 1
high = 100
steps = 0

print(f'Think of a number between {low} and {high}, and I\'ll try to guess it.')
print("Respond with 'less' if your number is lower, 'more' if it's higher and 'guessed' if I got it right.")


while True:
    guess = (low + high) // 2
    print(f'Is it {guess}?')
    feedback = input('Answer: ')

    steps += 1

    if feedback == 'guessed':
        print(f'Hurray! I\'ve guessed the number in {steps} attempts.')
        break
    elif feedback == 'less':
        high = guess - 1
    elif feedback == 'more':
        low = guess + 1
    else:
        print('Sorry! I did\'t understand your response. Please make sure you\'re giving the correct hints.')

    if low > high:
        print('Something seems to have gone wrong.')
        break
