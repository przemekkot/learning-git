num = 30
fibonacci = [1, 1]
counter = 1

for number in fibonacci:
  number = fibonacci[-1] + fibonacci[-2]
  counter += 1
  if counter == 30:
    break
  fibonacci.append(number)
  
print(fibonacci)

print(' ')
print("Powyzszy wynik to rezultat Ciagu Fibonacciego dla pierwszych 30 liczb")
