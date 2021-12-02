import maude
import sys
import ctypes
libmaude = ctypes.CDLL('libmaude.so')
libmaude._ZN10IO_Manager11setAutoWrapEb(
	libmaude.ioManager,
	ctypes.c_bool(False)
)

def main(filename):
    programFile = open(filename, "r").read()

    system = " < system : System |{ print(\"\"); print(\"\"); ${program} println(\"\"); | none } > "
    generatedSystem = system.replace("${program}", programFile)

    maude.init()
    maude.load("src/loads.maude")
    maude.getModule('SEMANTICS').parseTerm(generatedSystem).erewrite()

if __name__ == "__main__":
    main(sys.argv[1])