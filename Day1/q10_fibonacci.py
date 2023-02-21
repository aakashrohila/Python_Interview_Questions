# 10.Write a function to calculate the nth Fibonacci number.


def fibonacci(num):
    mt_list = [1,1]

    if num < 3:
        return mt_list

    else:

        for i in range(num):

            mt_list.append(mt_list[i] + mt_list[i+1])

            if len(mt_list) >= num:
                break

        return mt_list

x = int(input("Enter a number: "))

y = fibonacci(x)

print(y)
print(x,"th fibonnaci number is",y[x-1])