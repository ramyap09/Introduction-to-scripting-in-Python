"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.
"""


import csv
import math
import pygal


def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    list_of_tups = list(filter(lambda tup: tup[1] in gdp_countries,   plot_countries.items()))
    out_dict = dict(list_of_tups)
    l_of_tups = list(filter(lambda tup: tup[1] not in gdp_countries,  plot_countries.items()))
    out_set = set([item[0] for item in l_of_tups])
    return out_dict, out_set



def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    country_gdp_dict = {}
    country_nodata_for_year = set()
    diction = {}
    with open(gdpinfo["gdpfile"],"r", newline="") as fhand:
        csvread =  csv.DictReader(fhand, skipinitialspace = True, delimiter = gdpinfo["separator"], quotechar=gdpinfo["quote"])
        for item in csvread:
            diction[item[gdpinfo["country_name"]]] = item
    fn_dict, fn_set = reconcile_countries_by_name(plot_countries, diction)
    for key,value in fn_dict.items():
        if diction[value][year] == "":
            country_nodata_for_year.add(key)
        else:
            country_gdp_dict[key] = math.log10(float(diction[value][year]))

    return country_gdp_dict, fn_set, country_nodata_for_year




def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    country_gdp_dict, fn_set, country_nodata_for_year = build_map_dict_by_name(gdpinfo, plot_countries, year)

    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'GDP by Country for the year {} (log scale), unified by common country name'.format(year)
    worldmap_chart.add('GDP for {}'.format(year), country_gdp_dict)
    worldmap_chart.add("NO GDP data countries", fn_set)
    worldmap_chart.add("Data missing for the year {}".format(year), country_nodata_for_year)
    worldmap_chart.render_to_file(map_file)

    return



def test_render_world_map():
    """
    Test the project code for several years.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")



test_render_world_map()
