import sys

# code → string that represents the 3 letter code 
# values → chi dihedral values

# To run from the command line, type py definitions.py {AMINO_ACID HERE} {chi values here}
# Example: py definitions.py MET 62 180 68 180

def define(code, values):
    output = []
    try:
        output.append(chi1(code,values[0]))
    except IndexError:
        output.append("")
    try:
        output.append(chi2(code,values[1]))
    except IndexError:
        output.append("")
    try:
        output.append(chi3(code,values[2]))
    except IndexError:
        output.append("")
    try:
        output.append(chi4(code,values[3]))
    except IndexError:
        output.append("")
    try:
        output.append(chi5(code,values[4]))
    except IndexError:
        output.append("")
    return "".join(output)

def chi1(name, angle):
    if name in ["ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "HIS", "ILE",
                              "LEU", "LYS", "MET", "PHE", "SER", "THR", "TRP", "TYR", 
                              "VAL"]:
        if (angle >= 0) and (angle < 120):
            return "G+"
        elif (angle >= 120) and (angle < 240):
            return "T"
        elif (angle >= -120) and (angle < 0):
            return "G-"
    elif name == "PRO":
        if angle >= 0:
            return "G+"
        else:
            return "G-"
    else:
        return ""
        
def chi2(name, angle):
    if name in ["ARG", "GLN", "GLU", "ILE", "LEU", "LYS", "MET"]:
        if (angle >= 0) and (angle < 120):
            return "G+"
        elif (angle >= 120) and (angle < 240):
            return "T"
        elif (angle >= -120) and (angle < 0):
            return "G-"
    elif name in ["ASN", "ASP"]:
        if (angle >= 30) and (angle < 90):
            return "G+"
        elif (angle >= -30) and (angle < 30):
            return "T"
        elif (angle >= -90) and (angle < -30):
            return "G-"
    elif name in ["PHE", "TYR", "HIS"]:
        if (angle >= 30) and (angle < 150):
            return "G"
        if (angle >= -30) and (angle < 30):
            return "T"
    elif name == "TRP":
        if (angle >= -180) and (angle < -60):
            return "G+"
        elif (angle >= -60) and (angle < 60):
            return "T"
        elif (angle >= 60) and (angle < 180):
            return "G-"
    else:
        return ""

def chi3(name, angle):
    if name in ["ARG", "LYS", "MET"]:
        if (angle >= 0) and (angle < 120):
            return "G+"
        elif (angle >= 120) and (angle < 240):
            return "T"
        elif (angle >= -120) and (angle < 0):
            return "G-"
    elif name == "GLN" or name == "GLU":
        if (angle >= 30) and (angle < 90):
            return "G+"
        elif (angle >= -30) and (angle < 30):
            return "T"
        elif (angle >= -90) and (angle < -30):
            return "G-"
    else:
        return ""

def chi4(name, angle):
    if name in ["ARG", "LYS"]:
        if (angle >= 0) and (angle < 120):
            return "G+"
        elif (angle >= 120) and (angle < 240):
            return "T"
        elif (angle >= -120) and (angle < 0):
            return "G-"
    else:
        return ""

def chi5(name, angle):
    if name == "ARG":
        if (angle >= 0) and (angle < 120):
            return "G+"
        elif (angle >= 120) and (angle < 240):
            return "T"
        elif (angle >= -120) and (angle < 0):
            return "G-"
    else:
        return ""

if __name__ == "__main__":
    print(define(sys.argv[1], [int(x) for x in sys.argv[2:]]))
    

