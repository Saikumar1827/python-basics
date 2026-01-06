t = ()
t1 = tuple()

sample = ("172.10.33.25", "172.10.33.26", True, 123, 1234.56, 1234.567)
# print(type(sample), sample)

# tuple is immutable
# print(sample[0])
# sample[0] = 12
# print(sample)
# print(sample[0:2])
# print(sample[-1])

envs_list = ("DEV", "QA", "PREPROD", "PROD")

# print(dir(tuple))

"""
['count', 'index']
"""
sample = (1, 2, 3, 4, 5, 5, 6)
print(sample.count(5), sample.count(12))
print(sample.index(5))

# Type casting: Data type conversion
sample = ("172.10.33.25", "172.10.33.26", True, 123, 1234.56, 1234.567)
sample_1 = list(sample)
print(type(sample_1))
sample_2 = tuple(sample_1)
print(type(sample_2))