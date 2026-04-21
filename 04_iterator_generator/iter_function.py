import csv
from operator import ne


roles = ("user", "admin", "sysadmin")

roles_iterator = iter(roles)
print(next(roles_iterator))
print(next(roles_iterator))
print(next(roles_iterator))
# StopIteration
# print(next(roles_iterator))


def counter(n):
    for i in range(n):
        yield i


gen = counter(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# StopIteration
# print(next(gen))


def generate_id(start):
    id = start
    while True:
        yield id
        id += 1


# def generate_id():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5


id_generator = generate_id(1)
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))


def read_csv_with_gen(file_path):
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row


csv_gen = read_csv_with_gen("MOCK_DATA.csv")
# print(next(csv_gen))
# print(next(csv_gen))
# print(next(csv_gen))
# print(next(csv_gen))
for row in csv_gen:
    print(row)
