from enum import Enum

from pandera import Column, DataFrameSchema


class ImportTables(Enum):
    DOMESTIC_CONSUMPTION = "coffee_domestic_consumption"
    EXPORT = "coffee_export"
    INVENTORY = "coffee_green_coffee_inventorie"
    IMPORT = "coffee_import"
    IMPORTERS_CONSUMPTION = "coffee_importers_consumption"
    PRODUCTION = "coffee_production"
    RE_EXPORT = "coffee_re_export"


DOMESTIC_CONSUMPTION_SCHEMA = DataFrameSchema(
    {
        "Country": Column(str),
        "Coffee type": Column(object),
        "1990/91": Column(int),
        "1991/92": Column(int),
        "1992/93": Column(int),
        "1993/94": Column(int),
        "1994/95": Column(int),
        "1995/96": Column(int),
        "1996/97": Column(int),
        "1997/98": Column(int),
        "1998/99": Column(int),
        "1999/00": Column(int),
        "2000/01": Column(int),
        "2001/02": Column(int),
        "2002/03": Column(int),
        "2003/04": Column(int),
        "2004/05": Column(int),
        "2005/06": Column(int),
        "2006/07": Column(int),
        "2007/08": Column(int),
        "2008/09": Column(int),
        "2009/10": Column(int),
        "2010/11": Column(int),
        "2011/12": Column(int),
        "2012/13": Column(int),
        "2013/14": Column(int),
        "2014/15": Column(int),
        "2015/16": Column(int),
        "2016/17": Column(int),
        "2017/18": Column(int),
        "2018/19": Column(int),
        "2019/20": Column(int),
        "Total_domestic_consumption": Column(int),
    }
)

YEAR_SCHEMA = DataFrameSchema(
    {
        "Country": Column(object),
        "1990": Column(int),
        "1991": Column(int),
        "1992": Column(int),
        "1993": Column(int),
        "1994": Column(int),
        "1995": Column(int),
        "1996": Column(int),
        "1997": Column(int),
        "1998": Column(int),
        "1999": Column(int),
        "2000": Column(int),
        "2001": Column(int),
        "2002": Column(int),
        "2003": Column(int),
        "2004": Column(int),
        "2005": Column(int),
        "2006": Column(int),
        "2007": Column(int),
        "2008": Column(int),
        "2009": Column(int),
        "2010": Column(int),
        "2011": Column(int),
        "2012": Column(int),
        "2013": Column(int),
        "2014": Column(int),
        "2015": Column(int),
        "2016": Column(int),
        "2017": Column(int),
        "2018": Column(int),
        "2019": Column(int),
    }
)

EXPORT_SCHEMA = YEAR_SCHEMA.add_columns({"Total_export": Column(int)})

INVENTORIE_SCHEMA = YEAR_SCHEMA.add_columns({"Total_inventorie": Column(int)})

IMPORTERS_CONSUMPTION_SCHEMA = YEAR_SCHEMA.add_columns(
    {"Total_import_consumption": Column(int)}
)

IMPORT_SCHEMA = YEAR_SCHEMA.add_columns({"Total_import": Column(int)})

PRODUCTION_SCHEMA = DataFrameSchema(
    {
        "Country": Column(str),
        "Coffee type": Column(object),
        "1990/91": Column(float),
        "1991/92": Column(float),
        "1992/93": Column(float),
        "1993/94": Column(float),
        "1994/95": Column(float),
        "1995/96": Column(float),
        "1996/97": Column(float),
        "1997/98": Column(float),
        "1998/99": Column(float),
        "1999/00": Column(float),
        "2000/01": Column(float),
        "2001/02": Column(float),
        "2002/03": Column(float),
        "2003/04": Column(float),
        "2004/05": Column(float),
        "2005/06": Column(float),
        "2006/07": Column(float),
        "2007/08": Column(float),
        "2008/09": Column(float),
        "2009/10": Column(float),
        "2010/11": Column(float),
        "2011/12": Column(float),
        "2012/13": Column(float),
        "2013/14": Column(float),
        "2014/15": Column(float),
        "2015/16": Column(float),
        "2016/17": Column(float),
        "2017/18": Column(float),
        "2018/19": Column(float),
        "2019/20": Column(float),
        "Total_production": Column(float),
    }
)

RE_EXPORT_SCHEMA = YEAR_SCHEMA.add_columns({"Total_re_export": Column(int)})
