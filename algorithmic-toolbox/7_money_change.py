def get_change(m):
    number_of_coins = (m//10) + ((m%10)//5) + (m%5)
    return number_of_coins

m = int(input())
print(get_change(m))
