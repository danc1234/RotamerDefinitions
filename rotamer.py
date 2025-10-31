class rotamer:
    dihedral = None # Dihedral is either an integer or float
    staggered_type = None # staggered_type is a String

    def __init__(self, residue): # Residue is a string that is 3 letters long
        self.residue = residue
        
    # Although Python doesn't have "private" variables, it's nice to have these accessor functions.
    def getResidue(self):
        return self.residue
    def getDihedral(self):
        return self.dihedral
    def getStaggeredType(self):
        return self.staggered_type

    # Modifier functions
    def setDihedral(self, angle):
        self.dihedral = angle
    def setStaggeredType(self, staggered):
        self.staggered_type = staggered 


if __name__ == "__main__":
    a = rotamer("Pro")
    a.setDihedral(50)
    a.setStaggeredType("G+")
    print(a.getDihedral())
    print(a.getStaggeredType())