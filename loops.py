
# forloop whileloop
# continue break

# value = 0

# while value < 10:
#     if value == 5:
#         break
#     print(value)
#     value = value + 1

# value = 0

# while value < 10:
#     if value == 5:
#         value = value + 1  # incrementing is very important
#         continue
#     print(value)
#     value = value + 1

sample = ["server1", "server2", "server3", "server4", 342]

# idx = 0

# while idx < len(sample):
#     print(sample[idx])
#     idx += 1 # idx = idx + 1

# in -> membership operator (checks whether that element is present or not)
# print(1 in sample)
# print("server1" in sample)

# idx -> iterator
# sample -> iterable
# for ele in sample:
#     print(ele)  # ele = element
# print(ele)

# access elements inside a list with index using for loop
# range, enumerate
# print(list(range(5)))

# for idx in range(len(sample)):
#     print(sample[idx])

# for idx in range(len(sample)):
#     ele = sample[idx]
#     print(idx, ele)

print (enumerate(sample))
for idx, val in enumerate(sample):
    print(idx,val)

# tuple unpacking
# a, b = (1, 2)
# print(a, b)
