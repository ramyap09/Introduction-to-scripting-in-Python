"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.
"""

import csv
import pygal


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    diction = {}
    with open(filename, "r", newline="") as fhand:
        csvread = csv.DictReader(fhand, skipinitialspace=False, delimiter = separator, quotechar=quote)
        for item in csvread:
            diction[item[keyfield]] = item
    return diction




def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output:
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    lst = []
    lst_of_tups = list(filter(lambda tup : tup[0].isdigit(), gdpdata.items()))
    for tup in lst_of_tups:
        if int(tup[0]) >= gdpinfo["min_year"] and int(tup[0]) <= gdpinfo["max_year"] \
                                                                and tup[1] != "" :
            lst.append((int(tup[0]),float(tup[1])))
        else:
            pass
    lst.sort(key = lambda x:x[0])
    return lst





def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    diction = {}
    nested_dict = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_name"], gdpinfo["separator"], gdpinfo["quote"])
    for country in country_list :
        if country in nested_dict:
            diction[country] = build_plot_values(gdpinfo, nested_dict[country])
        else:
            diction[country] = []
    return diction




def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    out_dict = build_plot_dict(gdpinfo, country_list)
    XYplot = pygal.XY(x_title='Year', y_title= 'GDP in current US dollars')
    XYplot.title = "Plot of GDP for select countries spanning 1960 to 2015"
    for key, value in out_dict.items():
        XYplot.add(key,value)
    XYplot.render_to_file(plot_file)

    return




def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
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

    render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["United Kingdom", "United States"],
                   "isp_gdp_xy_uk+usa.svg")



test_render_xy_plot()
