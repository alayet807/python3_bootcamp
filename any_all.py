"""
all return true if everything in the iterable is true
"""
people=["kho","kmo""kno"]
all(people)#true
all([people[0]=='k' for x in people]) #all er moddhe iterable pass kori,tai list dichi. return true

"""
any return true if anything in iterable is true
"""