def validateInput(cowID):
    return cowID.isdigit() and len(cowID) == 8 and cowID[0] != '0'