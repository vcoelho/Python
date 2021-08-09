import arcpy
aprx = arcpy.mp.ArcGISProject(r"<FUllPATH>\MyProject.aprx")




connectionInfoTarget = {'connection_info': {'database': 'C:\\Victor\\01969210\\'}, 
 'dataset': 'RoadCenterline', 
 'workspace_factory': 'Shape File'}

for m in aprx.listMaps():
    print("Map: {0} Layers".format(m.name))
    for lyr in m.listLayers():

        if (lyr.name == "RoadCenterline"):
            connectionInfoOrigin = lyr.connectionProperties
            lyr.updateConnectionProperties(connectionInfoOrigin,connectionInfoTarget) 
        if lyr.isBroken:
            print("(BROKEN) " + lyr.name)
        else:
            print("  " + lyr.name)
            print("  " + lyr.dataSource)
            
del aprx
