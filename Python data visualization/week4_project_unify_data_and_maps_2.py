"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.
"""

import csv
import math
import pygal


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    diction = {}
    with open(codeinfo["codefile"],"r",newline="") as fhand:
        csvread = csv.DictReader(fhand, skipinitialspace=True, delimiter=codeinfo["separator"] ,quotechar=codeinfo["quote"])
        for item in csvread:
            diction[item[codeinfo["plot_codes"]]] = item[codeinfo["data_codes"]]
    return diction




def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    out_dict = {}
    out_set = set()
    country_code_conv_dict = build_country_code_converter(codeinfo)
    mod_country_code_con_dict =  dict([(k.lower(), v.lower()) for k, v in country_code_conv_dict.items()])
    for key in plot_countries.keys():
        for gdp_key in gdp_countries.keys() :
            if gdp_key.lower() == mod_country_code_con_dict.get(key.lower(),"") :
                out_dict[key] = gdp_key
            else:
                pass
        if mod_country_code_con_dict.get(key.lower(),"") not in [ele.lower() for ele in gdp_countries.keys()]:
            out_set.add(key)
    return out_dict, out_set




def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    diction = {}
    gdp_diction = {}
    output_dict = {}
    output_set1 = set()
    output_set2 = set()
    with open(gdpinfo["gdpfile"], "r", newline="") as fhand:
        csvread = csv.DictReader(fhand, skipinitialspace=True, delimiter = gdpinfo["separator"] , quotechar=gdpinfo["quote"] )
        for item in csvread:
            gdp_diction[item[gdpinfo["country_code"]]] = item

    out_dict, out_set = reconcile_countries_by_code(codeinfo, plot_countries, gdp_diction)

    for plot_code, gdp_code in out_dict.items() :
        if gdp_diction[gdp_code][year] == "" :
            output_set2.add(plot_code)
        else:
            output_dict[plot_code] = math.log10(float(gdp_diction[gdp_code][year]))

    output_set1 = out_set
    return output_dict, output_set1, output_set2




def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    output_dict, output_set1, output_set2 = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'GDP by Country for the year {} (log scale), unified by common country name'.format(year)
    worldmap_chart.add('GDP for {}'.format(year), output_dict)
    worldmap_chart.add("NO GDP data countries", output_set1)
    worldmap_chart.add("Data missing for the year {}".format(year), output_set2)
    worldmap_chart.render_to_file(map_file)
    return




def test_render_world_map():
    """
    Test the project code for several years
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year":1960,
        "max_year":2015,
        "country_name": "Country Name",
        "country_code":"Country Code"
    }

    codeinfo = {
        "codefile":"isp_country_codes.csv",
        "separator": ",",
        "quote": "'" , #'"',
        "plot_codes":"ISO3166-1-Alpha-2",
        "data_codes":"ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES


    # 1960
    render_world_map(gdpinfo, codeinfo, pygal_countries,  "1960", "isp_gdp_world_code_1960.svg")

    # 1980
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # 2000
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # 2010
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")



test_render_world_map()
