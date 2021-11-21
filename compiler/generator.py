import sys
import os
def main(filename):
    templateFile = open("compiler/template.maude", "r")
    programFile = open(filename, "r")
    program = programFile.read()
    template = templateFile.read()
    generated = template.replace("${program}", program)
    ouputFile = open("compiler/generated.maude", "w")
    ouputFile.write(generated)
    ouputFile.close()
    templateFile.close()
    programFile.close()
    os.system("maude.linux64 compiler/generated.maude")

if __name__ == "__main__":
    main(sys.argv[1])