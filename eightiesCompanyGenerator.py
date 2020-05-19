import time
import random

prefixes = [
	"Tele",
	"Electro",
	"Ener",
	"Alpha",
	"Beta",
	"Razer",
	"Conexto",
	"Magna",
	"Quant", 
	"Seque",
	"Micro",
	"Tri",
	"V",
	"Zeni",
	"Silver",
	"Therma", 
	"Ulta",
	"Bio",
	"Giga",
	"VFX",
	"Super",
	"Signa",
	"Cy",
	"Transma",
	"Sigma",
	"Adapta",
	"Opti",
	"Pana",
	"Nocta",
	"Cyber",
	"Aqua",
	"Paleo",
	"Thermo",
	"Hypa",
	"Cryo",
	"Fracta",
	"Spectra",
	"Fox",
	"Dyna",
	"Viva",
	"Cherry",
	"Q.X.I",
	"Oxy", 
	"Digi"
	"Patria"
 ]

suffixes = [
	"tron",
	"comp",
	"nex",
	"com",
	"vox",
	"star",
	"tex",
	"gem",
	"tec",
	"sonic",
	"byte",
	"tronics",
	"vid",
	"chip",
	"rix",
	"gen",
	"gate",
	"max",
	"trek",
	"ware",
	"Q",
	"ward",
	"trox",
	"cube",
	"disk",
	"spec"
]

end = [
	" Systems",
	" 3D",
	" Interactive",
	"-Link",
	" Robotics",
	" Gear",
	" Technology",
	" International",
	" Communications",
	" Group",
	" Power and Cooling",
	" Inc."
	" Design",
	" Corporation",
	" Memory",
	" Industries",
	" Semiconductors",
	" Intelligence",
	" Acoustics",
	"-Technica",
	" Dynamics",
	" Devices",
	" Audio",
	" Multimedia",
	" Computer Works",
	" Power",
	" LLC.",
	" Limited",
	" io"
]

def startSimulation():
	while(True):
		prefix = random.choice(prefixes)
		suffix = random.choice(suffixes)
		last = random.choice(end)
		print(prefix + suffix + last + "\n")
		time.sleep(3)

startSimulation()