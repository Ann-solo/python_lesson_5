def Prime_number(n):
    i=2
    while n>i:
        if n % i== 0:
            break
        i+=1
    return i==n

# print(Prime_number(n))


def all_dividers(n):
    all_div = []
    i=2
    while i*i<=n:
        if n%i==0:
            n//=i
            all_div.append(i)
        else:
            i+=1
    if n>1:
        all_div.append(n)
    return all_div

# print(all_dividers(n))


def biggest_div(n):
    big_div=all_dividers(n)
    max=0
    for i in big_div:
        if i > max:
            max=i
    return(max)

# print(biggest_div(n))


