
class management_tree:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    

def build_management_tree():
    director = management_tree("Anika", "Director")

    # Operations branch under Director
    rohan = management_tree("Rohan", "Operations Head")

    meera = management_tree("Meera", "Logistics Manager")
    meera.add_child(management_tree("Kunal", "Warehouse Supervisor"))
    meera.add_child(management_tree("Zara", "Fleet Coordinator"))

    tahir = management_tree("Tahir", "Quality Control Manager")
    rohan.add_child(meera)
    rohan.add_child(tahir)

    # Technology branch under Director
    samir = management_tree("Samir", "Technology Head")

    aisha = management_tree("Aisha", "Software Manager")
    aisha.add_child(management_tree("Dev", "Backend Lead"))
    aisha.add_child(management_tree("Nia", "Frontend Lead"))

    rehan = management_tree("Rehan", "Cybersecurity Manager")
    samir.add_child(aisha)
    samir.add_child(rehan)

    # Add both branches to the Director
    director.add_child(rohan)
    director.add_child(samir)

    return director
