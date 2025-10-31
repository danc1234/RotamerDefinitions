import Points

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
    def setStaggeredType(self): # These were taken from here: https://dunbrack.fccc.edu/bbdep2010/ConformationalAnalysis.php
        if self.residue == "Pro":
            if self.dihedral >= 0:
                self.staggered_type = "g+"
            else:
                self.staggered_type = "g-"
        else: 
            if self.dihedral >= 0 and self.dihedral < 120:
                self.staggered_type = "g+"
            elif self.dihedral >= 120 and self.dihedral < -120:
                self.staggered_type = "t"
            elif self.dihedral >= -120 and self.dihedral < 0:
                self.staggered_type = "g-" 

if __name__ == "__main__":
    a = rotamer("Ala")
    a.setDihedral(60)
    a.setStaggeredType()
    print(a.getDihedral())
    print(a.getStaggeredType())