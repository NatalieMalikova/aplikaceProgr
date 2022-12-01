from osgeo import ogr, osr
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFormLayout, QToolButton, QLineEdit,
                             QFileDialog, QWidget, QMenu, QAction)
from osgeo import osr

spatialRef = osr.SpatialReference()
spatialRef.ImportFromEPSG(2927)

source = osr.SpatialReference()
source.ImportFromEPSG(2927)

target = osr.SpatialReference()
target.ImportFromEPSG(4326)

transform = osr.CoordinateTransformation(source, target)

point = ogr.CreateGeometryFromWkt("POINT (1120351.57 741921.42)")
point.Transform(transform)

print(point.ExportToWkt())
