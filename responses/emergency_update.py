class Person:
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr
  
    def same(self, person):
        if self.name == person.get_name():
            return True
        else:
            return False
        
    def updated(self, person):
        if self.phone != person.get_phone() and self.addr != person.get_addr():
            return f'{self.get_name()} UPDATED BOTH'
        elif self.phone != person.get_phone():
            return f'{self.get_name()} UPDATED PHONE NUMBER'
        elif self.addr != person.get_addr():
            return f'{self.get_name()} UPDATED ADDRESS'
            
    
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    
    def get_addr(self):
        return self.addr
        

n_inputs = int(input())

for i in range(n_inputs):
    inp = [int(inp) for inp in input().split(' ')]
    old_cont = []
    for i in range(inp[0]):
        info = input().split(',')
        old_cont.append(Person(info[0], info[1], info[2]))
    new_cont = []
    for i in range(inp[1]):
        info = input().split(',')
        new_cont.append(Person(info[0], info[1], info[2]))
    
    output_arr = []
    for n_person in new_cont:
        created = True
        for o_person in old_cont:
            if n_person.same(o_person):
                updated = n_person.updated(o_person)
                if updated != None:
                    output_arr.append(updated)
                created = False
        if created:
            output_arr.append(f'{n_person.get_name()} CREATED')
    for o_person in old_cont:
        deleted = True
        for n_person in new_cont:
            if n_person.same(o_person):
                deleted = False
        if deleted:
            output_arr.append(f'{o_person.get_name()} DELETED')
        
    output_arr.sort()
    for out in output_arr:
        print(out)