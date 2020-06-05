from Hash_table.hash_table import MyHash

hash_table = MyHash(10)
hash_table.add_hash('Ivan Blagorodov', '999999999')
hash_table.add_hash('Sergey Fedorov', '7777777')
hash_table.add_hash('Vitaliy', '444444')
hash_table.add_hash('Alexandr', '222222')
hash_table.add_hash('Yaroslav', '111111111')

print(hash_table)