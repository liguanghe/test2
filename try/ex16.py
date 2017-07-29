target.open(ex16_test.txt)

print "I'M going to read these to the file."

target.read(line1)
target.read("\n")
target.read(line2)
target.read("\n")
target.read(line3)
target.read("\n")

print "And finally, we close it."
target.close()