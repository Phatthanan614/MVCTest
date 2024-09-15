from controller.readCSV import id_list,teats_list

def checkTeats(cowID):
    if cowID in id_list:
        idx = id_list.index(cowID)
        teats = teats_list[idx]
        if teats_list[idx] is None:
            teats = 0
        return teats
    