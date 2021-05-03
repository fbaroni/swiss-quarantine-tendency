import numpy
import pandas

csvFile = pandas.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

arrayCountries = numpy.array

for row in csvFile:
    print(row)