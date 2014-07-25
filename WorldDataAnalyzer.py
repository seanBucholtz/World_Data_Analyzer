## Sean Bucholtz
## CSC 110
## Section 3
## Assignment #8
## 6/10/13

# Reads file and compiles a master list of all data
def lines():
    
    data = open('WorldData.txt', 'r')
    line_master_list = []
    line = data.readline()
    
    while line != '':
        
        line_mod = line.rstrip()
        line_list = line_mod.split(',')
##        print(line_list) #trace
    
        for char in line_list:
            
            line_master_list.append(char)
    
        line = data.readline()
        
    data.close()
    return line_master_list

# Sorts master list into individual data specific lists   
def lists(l_master_list):
    
    l_country_list = []
    l_pop_list = []
    l_land_area_list = []
    l_pop_density_list = []

    for country in range(0,len(l_master_list),3):
        
        l_country_list.append(l_master_list[country])
##        print(l_country_list) #trace
    
    for pop in range(1,len(l_master_list),3):
        
        l_pop_list.append(float(l_master_list[pop]))
##        print(l_pop_list) #trace
    
    for land_a in range(2,len(l_master_list),3):
        
        l_land_area_list.append(float(l_master_list[land_a]))
##        print(l_land_area_list) #trace
    
    for num in range(len(l_pop_list)):
        
        pop_density = l_pop_list[num]/l_land_area_list[num]
        l_pop_density_list.append(pop_density)
##        print(l_pop_density_list) #trace
        
##    print(l_country_list) #trace Countries
##    print(l_pop_list) #trace Population
##    print(l_land_area_list) #trace Land Area      
##    print(l_pop_density_list) #trace Density
        
    return l_country_list,l_pop_list,l_land_area_list,l_pop_density_list

# Searches and returns highest and lowest value for a given parameter    
def high_low(data_list):
    
    highest_index = 0
    lowest_index = 0
    high = data_list[0]
    low = data_list[0]
    
    # finds Highest
    for num in range(1,len(data_list)):
        
        next_num = data_list[num]
##        print(high) #trace
##        print(next_num) #trace
        
        if high < next_num:
            
            high = data_list[num]
            highest_index = num
##            print(highest_index) #trace
            
    # finds Lowest
    for num in range(1,len(data_list)):
        
        next_num = data_list[num]
##        print(low) #trace
##        print(next_num) #trace
        
        if low > next_num:
            
            low = data_list[num]
            lowest_index = num
##            print(lowest_index) #trace
     
    return highest_index,lowest_index

# Calculates average for densities
def average(data_list):
    
    total = 0
    count = 0
    
    for num in data_list:
        
        total += num
        count += 1

    data_average = total/count

    return data_average

# Determines and returns which countries are dense and which are sparse
def dense_sparse(density,average,country):
    
    dense = []
    sparse = []
    
    for num in range(len(density)-1):

        if density[num] > (average*2):
            
            dense.append(country[num])

        elif density[num] < (average*(1/100)):
            
            sparse.append(country[num])

    return dense,sparse

def main():

    # variables
    master_list = lines()
##    print(master_list) #trace
    country_list,pop_list,land_area_list,pop_density_list = lists(master_list)
    highest_pop_index,lowest_pop_index = high_low(pop_list)
    greatest_land_index,least_land_index = high_low(land_area_list)
    highest_pop_density_index,\
                                lowest_pop_density_index = \
                                high_low(pop_density_list)
    average_pop_density = average(pop_density_list)
    dense_countries,sparse_countries = \
                                     dense_sparse(pop_density_list,\
                                                  average_pop_density,\
                                                  country_list)

    # output
    print('Welcome to Nation Aggregator\n\n')
    print('The total amount of countries in the list is', \
    str(len(country_list)) + '.\n')
    print('The total world population is', format(sum(pop_list), ',.0f') + \
          ' people.\n')
    print(country_list[highest_pop_index], \
    'has the highest population of', \
          format(pop_list[highest_pop_index], ',.0f') + ' people.\n')
    print(country_list[lowest_pop_index], \
          'has the lowest population of', \
          format(pop_list[lowest_pop_index], ',.0f') + ' people.\n')
    print(country_list[greatest_land_index], \
    'has the greatest amount of land at', \
          format(land_area_list[greatest_land_index], ',.0f'), 'sq. km.\n')
    print(country_list[least_land_index], \
          'has the least amount of land at', \
          format(land_area_list[least_land_index], ',.2f'), 'sq. km.\n')
    print(country_list[highest_pop_density_index], \
    'has the greatest population density of', \
          format(pop_density_list[highest_pop_density_index], ',.2f'), \
          'people per sq. km.\n')
    print(country_list[lowest_pop_density_index], \
          'has the lowest population density of', \
          format(pop_density_list[lowest_pop_density_index], ',.3f'), \
          'people per sq. km.\n')
    print('The average population density of the list is', \
          format(average_pop_density, ',.3f'), 'people per sq. km.\n')
    print(dense_countries, 'all have a population density that is more' +\
          ' than two times the average.\n')
    print(sparse_countries, 'all have a population density that is less' +\
          ' than 1% of the average population density.\n')

# START
main()

"""
### TEST

Testing performed with an abridged country list consisting of:
    Afghanistan,32358260,647500
    Germany,82162512,357021
    United States of America,313085380,9826630
    Russian Federation,142835555,17075200
    China,1347565324,9596960

Density: (people per sq. km) #hand calculated
    Afghanistan ~ 47.974
    Germany ~ 230.134
    United ~ States of America 31.86
    Russian Federation ~ 8.365
    China ~ 140.416

    Average ~ 91.75
    Average*2 ~ 183.5
    1% of average ~ 0.917

Expected output: #hand calculated
    Number of countries: 5
    World pop.: 1918007031
    Highest pop. country: China
    Lowest pop. country: Afghanistan
    Most land: Russian Federation
    Least land: Germany
    Greatest pop. density: Germany
    Lowest pop. density: Russian Federation
    Average density: ~ 91.75
    Countries w/ density > 2*AVG: Germany
    Countries w/ density < 1$ of AVG: none

Program output:
    Number of countries: 5 #congruent with expected output
    World pop.: 1918007031 #congruent with expected output
    Highest pop. country: China #congruent with expected output
    Lowest pop. country: Afghanistan #congruent with expected output
    Most land: Russian Federation #congruent with expected output
    Least land: Germany #congruent with expected output
    Greatest pop. density: Germany #congruent with expected output
    Lowest pop. density: Russian Federation ##congruent with expected output
    Average density: 92.150
    #congruent considering greater decimal places provide more accuracy
    Countries w/ density > 2*AVG: Germany #congruent with expected output
    Countries w/ density < 1$ of AVG: none #congruent with expected output
    #note - Eventhough no countries from the test case were produced
    in the sparse list, examining the density trace of the main (WorldData.txt)
    will blindly (w/o reference) show nations that will be on the sparse list

## Note: traces intentionally left in code (commented out) to allow for easy
reference and desired tracing

### END OF TEST    
"""


    
        

