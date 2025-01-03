from pathlib import Path 
uri = Path(r"D:\Tsubasa\Downloads\ne_50m_populated_places\ne_50m_populated_places.shp")
#uri = "Users/Tsubasa/Downloads/ne_50m_populated_places/ne_50m_populated_places.shp"
vlayer = iface.addVectorLayer(str(uri), "places", "ogr")

for feature in vlayer.getFeatures():
    print("{pop:.2f} mio people live in {name}".format(name = feature['NAME_EN'],
        pop = feature['POP_MAX']/1000000))
