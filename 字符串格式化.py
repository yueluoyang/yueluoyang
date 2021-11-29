print('{:>10}'.format('jfd'))
print('{:1^10}'.format('jfd'))
print('{:10f}'.format(123456))
print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'

# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

# 使用逗号为千位分隔符
print('{:,}'.format(1234567890))

#表示为百分数
points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))

# 使用特定类型的专属格式化
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))


# 两种更加复杂的例子
for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))

width = 5
for num in range(5,12): 
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()