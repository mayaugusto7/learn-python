# funcoes anonimas no python não tem o def
# Para criar funções anonimas devemos usar a expressão lambda

sum = lambda arg1, arg2: arg1 + arg2
print("Value of total: ", sum(10, 20))
print("Value of total: ", sum(20, 20))

def sum(arg1, arg2):
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total;

total = sum(10, 20)
print("Outside the function : ", total)
