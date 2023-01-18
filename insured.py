class Insured:

    def __init__(self,name, surename,age,phone):
        self.name = name
        self.surename = surename
        self.age = age
        self.phone = phone

    def __str__(self):
        return (f"{self.name}\t {self.surename}\t {self.age}\t {self.phone}\n")