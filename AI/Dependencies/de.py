print("All deppendencies installed!")
print("Please enter your AMD version.")

amd = input("AMD version -")

if "64" in amd:
    from subprocess import *
    Popen('64.bat')

elif "32" in amd:
    from subprocess import *
    Popen('32.bat')

else:
    print("Enter 32 or 64. For more information read Usermaual")

from subprocess import *
Popen('all.bat')
