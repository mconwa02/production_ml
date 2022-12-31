from enum import Enum

from schema import Schema


class ImportTables(Enum):
    DOMESTIC_CONSUMPTION = "coffee_domestic_consumption"
    EXPORT = "coffee_export"
    INVENTORY = "coffee_green_coffee_inventorie"
    IMPORT = "coffee_import"
    IMPORTERS_CONSUMPTION = "coffee_importers_consumption"
    PRODUCTION = "coffee_production"
    RE_EXPORT = "coffee_re_export"


DOMESTIC_CONSUMPTION_SCHEMA = Schema(
    {
        "Country": str,
        "Coffee type": object,
        "1990/91": int,
        "1991/92": int,
        "1992/93": int,
        "1993/94": int,
        "1994/95": int,
        "1995/96": int,
        "1996/97": int,
        "1997/98": int,
        "1998/99": int,
        "1999/00": int,
        "2000/01": int,
        "2001/02": int,
        "2002/03": int,
        "2003/04": int,
        "2004/05": int,
        "2005/06": int,
        "2006/07": int,
        "2007/08": int,
        "2008/09": int,
        "2009/10": int,
        "2010/11": int,
        "2011/12": int,
        "2012/13": int,
        "2013/14": int,
        "2014/15": int,
        "2015/16": int,
        "2016/17": int,
        "2017/18": int,
        "2018/19": int,
        "2019/20": int,
        "Total_domestic_consumption": int,
    }
)

COMMON_SCHEMA = Schema(
    {
        "Country": object,
        "1990": int,
        "1991": int,
        "1992": int,
        "1993": int,
        "1994": int,
        "1995": int,
        "1996": int,
        "1997": int,
        "1998": int,
        "1999": int,
        "2000": int,
        "2001": int,
        "2002": int,
        "2003": int,
        "2004": int,
        "2005": int,
        "2006": int,
        "2007": int,
        "2008": int,
        "2009": int,
        "2010": int,
        "2011": int,
        "2012": int,
        "2013": int,
        "2014": int,
        "2015": int,
        "2016": int,
        "2017": int,
        "2018": int,
        "2019": int,
    }
)

COFFEE_EXPORT_SCHEMA = Schema({**COMMON_SCHEMA.schema, "Total_export": int})

COFFEE_INVENTORIE_SCHEMA = Schema(
    {**COMMON_SCHEMA.schema, "Total_inventorie": int}
)

COFFEE_IMPORT_SCHEMA = Schema({**COMMON_SCHEMA.schema, "Total_import": int})

COFFEE_IMPORTERS_CONSUMPTION_SCHEMA = Schema(
    {**COMMON_SCHEMA.schema, "Total_import_consumption": int}
)

COFFEE_PRODUCTION_SCHEMA = Schema(
    {**COMMON_SCHEMA.schema, "Total_production": int}
)

COFFEE_RE_EXPORT_SCHEMA = Schema(
    {**COMMON_SCHEMA.schema, "Total_re_export": int}
)
