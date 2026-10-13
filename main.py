from pyscript import display, document

def checkMember(e):

    # just adding everyone in the class
    document.getElementById("checkOutput").innerHTML = ""
    members = ["GERTHY BAUSA", "SAVANNA BAUTISTA", "CARLOS BORROMEO", "ALEXA CUNANAN", "JOAQUIN CASTOR", "FAITH CONCEPCION", "ERAN DIAZ", "FRANCIS FERNANDEZ", "JARVIS JOVEN", "SAMANTHA LACUESTA", "NATHAN LADION", "BIANCA LEDRES", "LOUIE LEE", "ZARA LORENZO", "JERICHO MAGSALIN", "CHEREE MENDOZA", "FRANCHESCA PANGILINAN", "PHILIP PONCE", "CAITLIN RAMOS", "ANNE REYES", "TYLER SALES", "DANIELLE SANDOVAL", "PRINCESS SCHWAB", "JACOB SHERBURN", "GAVIN TAGUIGA", "JILLIANE TECH", "ARYANA VARGAS", "CALEB ESPIA", "PRINZ REYNOSO", "DEXTER REYES", "MATTHEW CORTEZ"]
    fName = document.getElementById("firstName").value.upper().strip() # make it not case sensitive and remove extra spaces
    lName = document.getElementById("lastName").value.upper().strip() # same thing here
    fullName = fName + " " + lName # combine to make full name
    check = fullName in members # check if fullName is in members
    wordsList = [f"Sorry {fullName}, you aren't part of the list. Re-check your input and try again!", f"Congratulations, {fullName}! You are a registered member of the ICT Club."] # list!!!!
    showOutput = wordsList[check] # index list with the boolean

    display(showOutput, target="checkOutput") # yay display