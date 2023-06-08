# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-06-08 12:37:49
"""
import arcpy
from arcpy.ia import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *

def MalheurPoderosaMod():  # MalheurPoderosaMod

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
    arcpy.CheckOutExtension("3D")

    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\GeoAnalytics Desktop Tools.tbx")
    lidar_CANOPY_HEIGHT_MODEL_MOSAIC_lyr = "D:\\Wild\\Ponderosa\\lidar_CANOPY_HEIGHT_MODEL_MOSAIC.lyr"
    MalheurNF_boundary = "D:\\Wild\\Ponderosa\\Ponderosa.gdb\\MalheurNF_boundary"

    # Process: Mosaic To New Raster (2) (Mosaic To New Raster) (management)
    New_DSM = arcpy.management.MosaicToNewRaster(input_rasters=[], output_location="", raster_dataset_name_with_extension="New_DSM.tif", coordinate_system_for_the_raster="PROJCS[\"NAD_1983_Oregon_Statewide_Lambert_Feet_Intl\",GEOGCS[\"GCS_North_American_1983\",DATUM[\"D_North_American_1983\",SPHEROID[\"GRS_1980\",6378137.0,298.257222101]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Lambert_Conformal_Conic\"],PARAMETER[\"False_Easting\",1312335.958005249],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",-120.5],PARAMETER[\"Standard_Parallel_1\",43.0],PARAMETER[\"Standard_Parallel_2\",45.5],PARAMETER[\"Latitude_Of_Origin\",41.75],UNIT[\"Foot\",0.3048]]", number_of_bands=None)[0]
    New_DSM = arcpy.Raster(New_DSM)

    # Process: Mosaic To New Raster (Mosaic To New Raster) (management)
    New_DEM = arcpy.management.MosaicToNewRaster(input_rasters=[], output_location="", raster_dataset_name_with_extension="", number_of_bands=None)[0]
    New_DEM = arcpy.Raster(New_DEM)

    # Process: Raster Calculator (Raster Calculator) (ia)
    new_canopymod = "D:\\Wild\\Wild.gdb\\new_canopymod"
    Raster_Calculator = new_canopymod
    new_canopymod =  New_DSM - New_DEM
    new_canopymod.save(Raster_Calculator)


    # Process: Aggregate Polygons (Aggregate Polygons) (cartography)
    Output_Feature_Class = ""
    Output_Table = ""
    arcpy.cartography.AggregatePolygons(in_features="", out_feature_class=Output_Feature_Class, aggregation_distance="", out_table=Output_Table)

    # Process: Extract by Attributes: Z=81feet (Extract by Attributes) (sa)
    Output_raster_3_ = ""
    Extract_by_Attributes_Z_81feet = Output_raster_3_
    Output_raster_3_ = arcpy.sa.ExtractByAttributes("", "")
    Output_raster_3_.save(Extract_by_Attributes_Z_81feet)


    # Process: Int (2) (Int) (3d)
    Output_raster = ""
    arcpy.ddd.Int(in_raster_or_constant=Output_raster_3_, out_raster=Output_raster)
    Output_raster = arcpy.Raster(Output_raster)

    # Process: Raster to Polygon (2) (Raster to Polygon) (conversion)
    Output_polygon_features_2_ = ""
    arcpy.conversion.RasterToPolygon(in_raster=Output_raster, out_polygon_features=Output_polygon_features_2_)

    # Process: Aggregate Polygons (2) (Aggregate Polygons) (cartography)
    Output_Feature_Class_2_ = ""
    Output_Table_2_ = ""
    arcpy.cartography.AggregatePolygons(in_features=Output_polygon_features_2_, out_feature_class=Output_Feature_Class_2_, aggregation_distance="", out_table=Output_Table_2_)

    # Process: Join Features (Join Features) (gapro)
    Output_Dataset = "D:\\Wild\\Wild.gdb\\RasterT_Int_Ma_AggregatePoly_JoinFeatures"
    arcpy.gapro.JoinFeatures(target_layer=Output_Feature_Class, join_layer=Output_Feature_Class_2_, output=Output_Dataset, join_operation="JOIN_ONE_TO_ONE")

    # Process: Extract by Mask (Extract by Mask) (sa)
    pondo_heightmod_1 = "D:\\Wild\\Wild.gdb\\pondo_heightmod_1"
    Extract_by_Mask = pondo_heightmod_1
    pondo_heightmod_1 = arcpy.sa.ExtractByMask(lidar_CANOPY_HEIGHT_MODEL_MOSAIC_lyr, MalheurNF_boundary, "INSIDE", "1565601.91915348 725633.745257162 1916475.31261048 1119476.3985661 PROJCS[\"NAD_1983_2011_Oregon_Statewide_Lambert_Ft_Intl\",GEOGCS[\"GCS_NAD_1983_2011\",DATUM[\"D_NAD_1983_2011\",SPHEROID[\"GRS_1980\",6378137.0,298.257222101]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Lambert_Conformal_Conic\"],PARAMETER[\"False_Easting\",1312335.958005249],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",-120.5],PARAMETER[\"Standard_Parallel_1\",43.0],PARAMETER[\"Standard_Parallel_2\",45.5],PARAMETER[\"Latitude_Of_Origin\",41.75],UNIT[\"Foot\",0.3048]],VERTCS[\"NAVD88_height_(ftUS)\",VDATUM[\"North_American_Vertical_Datum_1988\"],PARAMETER[\"Vertical_Shift\",0.0],PARAMETER[\"Direction\",1.0],UNIT[\"Foot_US\",0.3048006096012192]]")
    pondo_heightmod_1.save(Extract_by_Mask)


    # Process: Extract by Attributes (Extract by Attributes) (sa)
    Malheur_Pondo_CanopyMod = "D:\\Wild\\Wild.gdb\\Malheur_Pondo_CanopyMod"
    Extract_by_Attributes = Malheur_Pondo_CanopyMod
    Malheur_Pondo_CanopyMod = arcpy.sa.ExtractByAttributes(pondo_heightmod_1, "VALUE >= 81")
    Malheur_Pondo_CanopyMod.save(Extract_by_Attributes)


    # Process: Int (Int) (3d)
    Int_Malheur_Pondo_CanopyMod = "D:\\Wild\\Wild_1\\Wild_1.gdb\\Int_Malheur_Pondo_CanopyMod"
    arcpy.ddd.Int(in_raster_or_constant=Malheur_Pondo_CanopyMod, out_raster=Int_Malheur_Pondo_CanopyMod)
    Int_Malheur_Pondo_CanopyMod = arcpy.Raster(Int_Malheur_Pondo_CanopyMod)

    # Process: Raster to Polygon (3) (Raster to Polygon) (conversion)
    Malheur_CanopyMod_polygon_1 = "D:\\Wild\\Wild.gdb\\Malheur_CanopyMod_polygon_1"
    with arcpy.EnvManager(outputMFlag="Disabled", outputZFlag="Disabled"):
        arcpy.conversion.RasterToPolygon(in_raster=Int_Malheur_Pondo_CanopyMod, out_polygon_features=Malheur_CanopyMod_polygon_1, simplify="SIMPLIFY", raster_field="VALUE", create_multipart_features="SINGLE_OUTER_PART")

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="D:\\Wild\\Wild.gdb", workspace="D:\\Wild\\Wild.gdb"):
        MalheurPoderosaMod()
