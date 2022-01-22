import maude
import sys

def main(filename):
    programFile = open(filename, "r").read()
    initialProgram = "function 'main() { print(\"\"); print(\"\"); print(\"\"); "
    generatedProgramFile = programFile.replace("function 'main() {", initialProgram)

    system = " < system : System | { ${program} | none } > "
    generatedSystem = system.replace("${program}", generatedProgramFile)

    maude.init()
    maude.load("src/loads.maude")
    maude.getModule('SEMANTICS').parseTerm(generatedSystem).erewrite()

if __name__ == "__main__":
    main(sys.argv[1])