Project: Designing University of Texas at Arlington's map on GIS and Spatial Database System
Course: Advanced Database Systems CSE 6331, Spring 2018

Team: Section-G
Name of Team members: Mansoor Abbas Ali(1001453343) and Chirag Hareshkumar Shah(1001558825)

Directory Structure:
1. KML : Consists of complete UTA Map, where in all Building geometries are under "Polygons" folder tag, all Path LineStrings
are under "lines"  folder tag and Building Entrances are under "points" folder tag.
You can open the file in any text editor/Google MyMaps/ Google Earth Pro.

2. QGIS: Consists of complete QGIS project. The project is build with QGIS 2.18.17 version. It can be opened in QGIS Desktop 
and various layers and plugins can be browsed inside it.

3. Query UI: A query window was designed for making a custom window for running few Spatial query operations on 
UTA MAP. The UTA_QUERY_GUI.ui is placed inside folder PythonGui. GUI and script together can be utilized inside QGIS 
Python console and custome operation can be performed.  

4. Report: Consist of ADS project report. This document describes the entire project and provides an insight with QGIS and 
PostgreSQL workflow.

5. Shapefile: Consists of uta_paths.shp, uta_buildings.shp, uta_entrances.shp (with other extensions .prj,.qpj,.shx,.dbf) which 
were created to intermediary to convert KML files to shapefile and then were used to upload in PostgreSQL.

6. SQL: Consists of two files:
1. uta_map_sdb.backup file which is backup version of uta_map_sdb database used in the project. It can be recovered in PostgreSQL
and can be used.
2. uta_map_sdb.sql file which is SQL version of create and insert methods of uta_map_sdb database. 



			-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X- 


