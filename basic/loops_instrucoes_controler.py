# break Encerra a instrução de loop e transfere a execução para a instrução imediatamente após o loop.

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:
   print('Current variable value :', var)
   var = var -1
   if var == 5:
      break
print("Good bye!")

# continue Faz com que o loop pule o restante do corpo e teste novamente sua condição imediatamente antes de reiterar.

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:
   var = var -1
   if var == 5:
      continue
   print('Current variable value :', var)
print("Good bye!")

# pass A instrução pass no Python é usada quando uma instrução é necessária sintaticamente, mas você não deseja que
# nenhum comando ou código seja executado.

for letter in 'Python':
   if letter == 'h':
      pass
      print('This is pass block')
   print('Current Letter :', letter)
print("Good bye!")
