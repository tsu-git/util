from pathlib import Path 


uri = Path(r"D:\Tsubasa\Downloads\ne_50m_populated_places\ne_50m_populated_places.shp")
# Below code does not work. Do not use.
#uri = "Users/Tsubasa/Downloads/ne_50m_populated_places/ne_50m_populated_places.shp"

# Make layer
vlayer = iface.addVectorLayer(str(uri), "places", "ogr")

# Resize symbol
#vlayer.renderer().symbol().setSize(6)
#vlayer.trigger.Repaint()

# Reshape symbol
vlayer.renderer().symbol().symbolLayer(0).setShape(QgsSimpleMarkerSymbolLayerBase.Star)
vlayer.renderer().symbol().setSize(6)
vlayer.trigger.Repaint()


'''
for feature in vlayer.getFeatures():
    print("{pop:.2f} mio people live in {name}".format(name = feature['NAME_EN'],
        pop = feature['POP_MAX']/1000000))
'''