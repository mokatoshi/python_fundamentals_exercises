string = input()
repeating = int(input())

repeat_as_lambda = lambda word, times: word * times

print(repeat_as_lambda(string, repeating))
