# simple string program 

msg1 = 'hoopla'
print(msg1)

# string with special character

msg2 = 'he said, \let Us python \'.'
file1 = 'C:\\temp\\newfile'
file2 = r'C:\temp\ newfile' # raw string = prepand r 

print(msg2)
print(file1)
print(file2)

#multiline strings
#whitesspace at beginning of second line becomes part of string 

msg3 = 'what is this life if full care...\we have no time to stand and stare'

#  enter at the end of first line becomes part of string

msg4 = """what is this life if full care... we have no time to stand and stare"""

# strings are concantenated propely.() necessary

msg5 = ('what is this life if full care..' 'we have no time to stand and stare ')

print(msg3)
print(msg4)
print(msg5)

# string replication during printing 

mssg6 = 'maclearn!'
print(msg1 * 3)

#immutablability of strings
#utopia cannot change, msg7 can

msg7 = 'Utopia'
msg8 = 'Today!!!'
msg7 = msg7 + msg8  #concatenation using +
print(msg7)

# use of built - in function on string

print(len('hoopla'))
print(min('hoopla'))
