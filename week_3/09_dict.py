# 나의 풀이
# class Dict:
#     def __init__(self):
#         self.items = [None] * 8
#
#     def put(self, key, value):
#         put_dict = self.items[hash(key) % 8] = value
#         return put_dict
#
#     def get(self, key):
#         get_dict = self.items[hash(key) % 8]
#         return get_dict
#
# my_dict = Dict()
# my_dict.put("test", 3)
# print(my_dict.get("test"))

class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))