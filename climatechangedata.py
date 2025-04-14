import math
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
import numpy as np
import random

totalRecordedCO2Emissions = {} #Dictionary of the total documented CO2 emissions of each country and region of the world (in tonnes)
annualCO2PerCountry = open("annual-co2-emissions-per-country.csv", "r") #Entity,Code,Year,Annual CO₂ emissions
for line in annualCO2PerCountry:
    line = line.strip()
    line = line.split(",")
    if line[0] not in totalRecordedCO2Emissions:
        totalRecordedCO2Emissions[line[0]] = math.floor(float(line[3]))
    elif line[0] in totalRecordedCO2Emissions:
        totalRecordedCO2Emissions[line[0]] += math.floor(float(line[3]))
annualCO2PerCountry.close()


totalRecordedEmissionsPerSector = {} #Dictionary of dictionaries which show the total emissions per a country's sector (In tonnes)
ghgEmissionsBySector = open("ghg-emissions-by-sector.csv", "r") # Entity,Code,Year,Greenhouse gas emissions from agriculture,Greenhouse gas emissions from land use change and forestry,Greenhouse gas emissions from waste,Greenhouse gas emissions from buildings,Greenhouse gas emissions from industry,Greenhouse gas emissions from manufacturing and construction,Greenhouse gas emissions from transport,Greenhouse gas emissions from electricity and heat,Fugitive emissions of greenhouse gases from energy production,Greenhouse gas emissions from other fuel combustion,Greenhouse gas emissions from bunker fuels
for line in ghgEmissionsBySector:
    line = line.strip()
    line = line.split(",")
    if line[0] not in totalRecordedEmissionsPerSector:
        totalRecordedEmissionsPerSector[line[0]] = ""
ghgEmissionsBySector.close()
for country in totalRecordedEmissionsPerSector:
    ghgEmissionsBySector = open("ghg-emissions-by-sector.csv", "r")
    totalemissionsbysector = {}
    totalemissionsbysectorlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in ghgEmissionsBySector:
        line = line.strip()
        line = line.split(",")
        if line[0] == country:
            for sector in range(3, 14):
                if sector == 3 and line[3] != "":
                    totalemissionsbysectorlist[0] += math.floor(float(line[3]))
                elif sector == 4 and line[4] != "":
                    totalemissionsbysectorlist[1] += math.floor(float(line[4]))
                elif sector == 5 and line[5] != "":
                    totalemissionsbysectorlist[2] += math.floor(float(line[5]))
                elif sector == 6 and line[6] != "":
                    totalemissionsbysectorlist[3] += math.floor(float(line[6]))
                elif sector == 7 and line[7] != "":
                    totalemissionsbysectorlist[4] += math.floor(float(line[7]))
                elif sector == 8 and line[8] != "":
                    totalemissionsbysectorlist[5] += math.floor(float(line[8]))
                elif sector == 9 and line[9] != "":
                    totalemissionsbysectorlist[6] += math.floor(float(line[9]))
                elif sector == 10 and line[10] != "":
                    totalemissionsbysectorlist[7] += math.floor(float(line[10]))
                elif sector == 11 and line[11] != "":
                    totalemissionsbysectorlist[8] += math.floor(float(line[11]))
                elif sector == 12 and line[12] != "":
                    totalemissionsbysectorlist[9] += math.floor(float(line[12]))
                elif sector == 13 and line[13] != "":
                    totalemissionsbysectorlist[10] += math.floor(float(line[13]))
    totalemissionsbysector["Agriculture"] = totalemissionsbysectorlist[0]
    totalemissionsbysector["Land Use and Forestry"] = totalemissionsbysectorlist[1]
    totalemissionsbysector["Waste"] = totalemissionsbysectorlist[2]
    totalemissionsbysector["Buildings"] = totalemissionsbysectorlist[3]
    totalemissionsbysector["Industry"] = totalemissionsbysectorlist[4]
    totalemissionsbysector["Manufacturing and Construction"] = totalemissionsbysectorlist[5]
    totalemissionsbysector["Transport"] = totalemissionsbysectorlist[6]
    totalemissionsbysector["Electricity and Heat"] = totalemissionsbysectorlist[7]
    totalemissionsbysector["Energy Production"] = totalemissionsbysectorlist[8]
    totalemissionsbysector["Other Fuel Combustion"] = totalemissionsbysectorlist[9]
    totalemissionsbysector["Bunker Fuels"] = totalemissionsbysectorlist[10]
    totalRecordedEmissionsPerSector[country] = totalemissionsbysector
    ghgEmissionsBySector.close()

mostContributingSectorPerCountry = {} # Dictonary of which sector contributes the most ghg emissions per every country
for country in totalRecordedEmissionsPerSector:
    comparelist = []
    for sector in totalRecordedEmissionsPerSector[country].values():
        comparelist.append(sector)
    comparelist.sort(reverse=True)
    mostContributingSectorPerCountry[country] = list(totalRecordedEmissionsPerSector[country].keys())[list(totalRecordedEmissionsPerSector[country].values()).index(comparelist[0])]
 

ppmPerYear = {} # Dictionary of years and the ppm of CO2 in the atmosphere (CO2 is primarily used as the measurement basis as it is easy to detect and the makes up the majority of ghg emissions)
ppmPerYearFile = open("co2_mm_mlo.txt", "r")
#            decimal       monthly    de-season  #days  st.dev  unc. of
#             date         average     alized          of days  mon mean
for line in ppmPerYearFile:
    line = line.split(" ")
    cleanline = []
    for i in line:
        if i != "":
            i.strip()
            cleanline.append(i)
    line = cleanline
    ppmPerYear[line[1]+"/"+line[0]] = float(line[3])
ppmPerYearFile.close()
# Proper credit and info for the file:
# --------------------------------------------------------------------
# USE OF NOAA GML DATA
# 
# These data are made freely available to the public and the scientific
# community in the belief that their wide dissemination will lead to
# greater understanding and new scientific insights. To ensure that GML
# receives fair credit for their work please include relevant citation
# text in publications. We encourage users to contact the data providers,
# who can provide detailed information about the measurements and
# scientific insight.  In cases where the data are central to a
# publication, coauthorship for data providers may be appropriate.
# 
# 
# 
# Contact:  Xin Lan (xin.lan@noaa.gov)
# 
# File Creation: Fri Mar 14 08:56:05 2025
# 
# 
# --------------------------------------------------------------------
# 
# 
# See gml.noaa.gov/ccgg/trends/ for additional details.
# 
# Data from March 1958 through April 1974 have been obtained by C. David Keeling
# of the Scripps Institution of Oceanography (SIO) and were obtained from the
# Scripps website (scrippsco2.ucsd.edu).
# Monthly mean CO2 constructed from daily mean values.
# Scripps data downloaded from http://scrippsco2.ucsd.edu/data/atmospheric_co2
# Monthly values are corrected to center of month based on average seasonal
# cycle. Missing days can be asymmetric which would produce a high or low bias.
# Missing months have been interpolated, for NOAA data indicated by negative stdev
# and uncertainty. We have no information for SIO data about Ndays, stdv, unc
# so that they are also indicated by negative numbers
#
# NOTE: Due to the eruption of the Mauna Loa Volcano, measurements from Mauna Loa Observatory
# were suspended as of Nov. 29, 2022 and resumed in July 2023. 
# Observations starting from December 2022 to July 4, 2023 are from a site at the 
# Maunakea Observatories, approximately 21 miles north of the Mauna Loa Observatory.


TemperatureDifferencePerYear = {} # Dictionary of years and the temperature difference between the 1950-80s average (in Celsius)
TemperatureDifferenceFile = open("global_land-ocean_temp.txt", "r")
#Land-Ocean Temperature Index (C)
#--------------------------------
#Year No_Smoothing  Lowess(5)
#----------------------------
for line in TemperatureDifferenceFile:
    line = line.split(" ")
    cleanline = []
    for i in line:
        if i != "":
            i.strip()
            cleanline.append(i)
        line = cleanline
    TemperatureDifferencePerYear[int(line[0])] = float(line[1])
# Credits to NASA for the file above



# Figures
def sectorsPieChart(x, y, country, figure):
    total = sum(totalRecordedEmissionsPerSector[country].values())
    index = 0
    cumulative_angle = 0
    for i in totalRecordedEmissionsPerSector[country].values():
        figure.annular_wedge(x, y, 1, 0, cumulative_angle, 6.28*(i/total)+cumulative_angle, "anticlock", color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), legend_label = list(totalRecordedEmissionsPerSector[country])[list(totalRecordedEmissionsPerSector[country].values()).index(i)])
        cumulative_angle += 6.28*(i/total)
        index += 1

pieChartFigures = []
for entity in totalRecordedEmissionsPerSector:
    if sum(totalRecordedEmissionsPerSector[entity].values()) > 0:
        piefigure = figure(title = "Breakdown of " + entity + "'s " + " Emissions by Sector") #WIP
        sectorsPieChart(1, 1, entity, piefigure)
        pieChartFigures.append(piefigure)


f2 = figure(title = "Average PPM of Co2 per Year")
f2.xaxis.axis_label = "Year"
f2.yaxis.axis_label = "Average CO2 in the Atmosphere (ppm)"
f2xVals = []
buffer = 3/12
for i in range(len(ppmPerYear)):
    f2xVals.append(1958 + buffer)
    buffer += 1/12
f2.line(f2xVals, list(ppmPerYear.values()), line_width = 1, color = "black")


f3 = figure(title = "Temperature Difference per Year (compared to the 1950-80 average)")
f3.xaxis.axis_label = "Year"
f3.yaxis.axis_label = "Temperature Difference (C)"
f3.vbar(list(TemperatureDifferencePerYear), 0.9, list(TemperatureDifferencePerYear.values()))


f4 = figure(title = "Top 50 Contributing Entities to CO2 Emissions")
f4.xaxis.axis_label = "Entity"
f4.yaxis.axis_label = "Total Recorded CO2 Emissions (tonnes)"
sortedTotalCO2Emissions = list(totalRecordedCO2Emissions.values())
sortedTotalCO2Emissions.sort(reverse=True)
f4YVals = []
f4Names = []
for i in sortedTotalCO2Emissions[:50]:
    f4YVals.append(i)
    f4Names.append(list(totalRecordedCO2Emissions)[list(totalRecordedCO2Emissions.values()).index(i)])
f4.vbar(list(range(0, 101, 2)), 1, f4YVals)
f4.text(list(range(0, 101, 2)), -0.5, f4Names, math.pi/2*-1, font_size = "8px")

display = [[f2, f3, f4], []]
count = 0
for i in pieChartFigures:
    if count <= 3:
        display[-1].append(i)
        count +=1
    elif count > 3:
        count = 0
        display[-1].append(i)
        display.append([])


# Final Display
ff = gridplot(display)
show(ff)