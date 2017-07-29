
import hashmap
# create a mapping of state to abbrevition
states = hashmap.new()
	hashmap.set(states, 'Oregen': 'OR')
	hashmap.set(states, 'Florida': 'FL')
	hashmap.set(states, 'California': 'CA')
	hashmap.set(states, 'New Your': 'NY')
	hashmap.set(states, 'Michigan': 'MI')


# create a basic set of states and some cities in them
cities = hashmap.new()
	hashmap.set(cityies, 'CA': 'San Francisco')
	hashmap.set(cityies'MI': 'Detroit')
	hashmap.set(cityies'FL': 'Jacksonville')


# add some more cities
hashmap.set(cities['NY'] = 'New York')
hashmap.set(cityies['OR'] = 'Portland')


# print out some cities
print '-' * 10
print "NY State has: ", hashmap.set(cities,'NY')
print "OR State has: ", hashmap.set(cityies,'OR')


# print some states
print '-' * 10
print "Michigan's abbreviation is: ", % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: ", % hashmap.get(states,'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", hashmap.get(cities,hashmap.get(states,'Michigan'))
print "Florida has: ", hashmap.get(cities, hashmap.get(states,'Florida'))

# print every state abbreviation 
print '-' * 10
hashmap.list(states)

	
# print every city in state
print '-' * 10
hashmap.list(cities)

	
# now do both at hte same time
print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
	print "Sorry, no Texas."
	
# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city