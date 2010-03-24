from sqlalchemy import func, literal
from geoalchemy.base import GeometryBase, SpatialComparator, _to_gis, SpatialElement, WKTSpatialElement, WKBSpatialElement
#from geoalchemy.geometry import Geometry

class SFSComparator(SpatialComparator):
    """Spatial Comparators for implementing Geometry Relationships
    for OGC SFS geometries.
    """
    
    @staticmethod
    def geom_from_wkb(geom):
        """This method is used for relation functions that take two geometries.
        According to the type of geom, a conversion to the database geometry type is added.
            
        """
        if isinstance(geom, SpatialElement):
            if isinstance(geom, WKTSpatialElement):
                return func.GeomFromText(literal(geom.desc, GeometryBase), geom.srid)
            if isinstance(geom, WKBSpatialElement):
                return func.GeomFromWKB(literal(geom.desc, GeometryBase), geom.srid)  
            return func.GeomFromWKB(literal(geom.desc.desc, GeometryBase), geom.desc.srid)
        elif isinstance(geom, basestring):
            wkt = WKTSpatialElement(geom)
            return func.GeomFromText(literal(wkt, GeometryBase), wkt.srid)
            
        return literal(_to_gis(geom), GeometryBase)


    # Geometry relations using the spatial element geometry

    def equals(self, other):
        return func.Equals(self.__clause_element__(),
            SFSComparator.geom_from_wkb(other))

    def distance(self, other):
        return func.Distance(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def disjoint(self, other):
        return func.Disjoint(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def intersects(self, other):
        return func.Intersects(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def touches(self, other):
        return func.Touches(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def crosses(self, other):
        return func.Crosses(self.__clause_element__(),
    		SFSComparator.geom_from_wkb(other))

    def within(self, other):
        return func.Within(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def overlaps(self, other):
        return func.Overlaps(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def gcontains(self, other):
        return func.Contains(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    # Geometry relations using Minimum Bounding Rectangle (MBR)

    def mbr_equals(self, other):
        return func.MBREquals(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def mbr_distance(self, other):
        return func.MBRDistance(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def mbr_disjoint(self, other):
        return func.MBRDisjoint(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def mbr_intersects(self, other):
        return func.MBRIntersects(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def mbr_touches(self, other):
        return func.MBRTouches(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def mbr_within(self, other):
        return func.MBRWithin(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def mbr_overlaps(self, other):
        return func.MBROverlaps(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))

    def mbr_contains(self, other):
        return func.MBRContains(self.__clause_element__(),
			SFSComparator.geom_from_wkb(other))


class SQLMMComparator(SpatialComparator):
    """Spatial Comparators for implementing Geometry Relationships
    for OGC SQL/MM geometries.
    """

    @staticmethod
    def geom_from_wkb(geom):
        """This method is used for relation functions that take two geometries.
        According to the type of geom, a conversion to the database geometry type is added.
            
        """
        if isinstance(geom, SpatialElement):
            if isinstance(geom, WKTSpatialElement):
                return func.ST_GeomFromText(literal(geom.desc, GeometryBase), geom.srid)
            if isinstance(geom, WKBSpatialElement):
                return func.ST_GeomFromWKB(literal(geom.desc, GeometryBase), geom.srid)  
            return func.ST_GeomFromWKB(literal(geom.desc.desc, GeometryBase), geom.desc.srid)
        elif isinstance(geom, basestring):
            wkt = WKTSpatialElement(geom)
            return func.ST_GeomFromText(literal(wkt, GeometryBase), wkt.srid)
            
        return literal(_to_gis(geom), GeometryBase)
    
    def equals(self, other):
        return func.ST_Equals(self.__clause_element__(),
            SQLMMComparator.geom_from_wkb(other))

    def distance(self, other):
        return func.ST_Distance(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other))

    def within_distance(self, other, distance=0.0):
        return func.ST_DWithin(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other), distance)

    def disjoint(self, other):
        return func.ST_Disjoint(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other))

    def intersects(self, other):
        return func.ST_Intersects(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other))

    def touches(self, other):
        return func.ST_Touches(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other))

    def crosses(self, other):
        return func.ST_Crosses(self.__clause_element__(),
    		SQLMMComparator.geom_from_wkb(other))

    def within(self, other):
        return func.ST_Within(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other))

    def overlaps(self, other):
        return func.ST_Overlaps(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other))

    def gcontains(self, other):
        return func.ST_Contains(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other))

    def covers(self, other):
        return func.ST_Covers(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other))

    def covered_by(self, other):
        return func.ST_CoveredBy(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other))

    def intersection(self, other):
        return func.ST_Intersection(self.__clause_element__(),
			SQLMMComparator.geom_from_wkb(other))

