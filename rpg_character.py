# Character sheet generation settings
full_dot = '●'
empty_dot = '○'

# Collect user input for character details
name = input("Please enter your name: ")
strength = int(input("Please enter your strength: "))
intelligence = int(input("Please enter your intelligence: "))
charisma = int(input("Please enter your charisma: "))

# Validate character name constraints
if type(name) is not (str):
    print ("The character name should be a string.")
if name == "":
    print ("The character should have a name.")
if len(name) > 10:
    print ("The character name is too long.")
if " " in name:
    print ("The character name should not contain spaces.")
    
# Validate character attribute constraints and point allocations
if type(strength) is not (int) or type(intelligence) is not (int) or type(charisma) is not (int):
    print ("All stats should be integers.")
if strength < 1 or intelligence < 1 or charisma < 1:
    print ("All stats should be no less than 1.")
if strength > 4 or intelligence > 4 or charisma > 4:
    print ("All stats should be no more than 4.")
if not strength + intelligence + charisma == 7:
    print ("The character should start with 7 points.")

# Generate the visual stat bar for Strength (STR)
s = 'STR '
for i in range(strength):
    s += full_dot
for i in range(10 - strength):
    s += empty_dot

# Generate the visual stat bar for Intelligence (INT)
inte = 'INT '
for i in range(intelligence):
    inte += full_dot
for i in range(10 - intelligence):
    inte += empty_dot

# Generate the visual stat bar for Charisma (CHA)
c = 'CHA '
for i in range(charisma):
    c += full_dot
for i in range(10 - charisma):
    c += empty_dot 
        
# Output the completed character sheet to the console
print (name + "\n" + s + "\n" + inte + "\n" + c)
