server_1 = "172.10.33.22"
server_2 = "172.10.33.23"

servers = ["172.10.33.22", "172.10.33.23", True, 123, 1234.56, 1234.567]
print(servers)
# print(type(servers), servers, server_1, server_2)

# pythone is zero indexed based
server_1 = servers[0]
# print("server 1 IP address:", server_1)

# Slicing (start_index:end_index +1 step_size), end index in python is not inclusive
# step_size: 1 (default)
simple_slice = servers[1:6:2]  #[1, 1+2. 3+2, 5+2]
simple_slice = servers[1:]
print(simple_slice)
simple_slice = servers[:5]
print(simple_slice)
simple_slice = servers[:]
print(simple_slice)
# print(simple_slice)

# Negative indexing
simple_slice = servers[-1:-4:-1]
# print(simple_slice)

# print ("Length of list:", len(simple_slice))

# List is a mutable datatype
# print("Before modify:", servers)
servers[-3] = 1234  # Inplace operation
# print("After modification:", servers)

# print("List of operations:", dir(servers))

"""
 [ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

servers = ["172.10.33.22", "172.10.33.23", True, 123, 1234.56, 1234.567, True]
print("Before:", servers)
servers.append (False)
print("After:", servers)
servers.append (["a", "b"])
print("After:", servers)
print("After append:", servers, len(servers) )
# Multi indexing
# print(servers[-1][0])
servers.extend(["c", "d"])
print("After extend:", servers, len(servers) )
print(servers.index (True))
servers.insert(0,12)
print(servers)
servers.remove(True)
print(servers)
servers.reverse()
print(servers)
servers = servers[::-1]
print(servers)

# Sort
servers = [1, 4, 7, 8, 2, 5]
# servers.sort()
server_1 = sorted(servers)
print(servers, server_1)

servers = ["172.10.33.22", "172.10.33.23", True, 123, 1234.56, 1234.567, True]
server_1 = servers.copy()
server_1.remove(123)
print(servers, server_1)
