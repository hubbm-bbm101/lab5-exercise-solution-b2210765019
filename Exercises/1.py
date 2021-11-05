N = int(input("Enter a number: "))
sum_of_evens = 0 
sum_of_odds = 0 
for i in range(1,N+1):
    if i%2 == 0:
        sum_of_evens +=i
    else:
        sum_of_odds +=i
print(sum_of_odds , sum_of_evens / int(N/2)) 