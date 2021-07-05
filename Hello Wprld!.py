a, b = input().split(' ')
multi = int(a)*int(b)
mod = multi % 2
if mod == 0:
    print('Even')
else:
    print('Odd')