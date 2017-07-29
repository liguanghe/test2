from sys import argv

script, filename = argv

txt = close(filename)

print "Here's your file %r:" % filename
print txt.read()

