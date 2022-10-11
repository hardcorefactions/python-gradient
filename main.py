from colour import Color
from PIL import ImageColor

RESET = '\033[0m'

def printg(text, c1, c2):
	def get_color_escape(r, g, b, background=False):
		return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

	def get_rgb_code(hex):
		return ImageColor.getcolor(hex, "RGB")

	c1 = Color(c1)
	c2 = Color(c2)
	lt = len(text)
	cl = list(c1.range_to(c2,lt))
	col=0
	ft = ""
	for i in cl:
		i = str(get_rgb_code(str(i))).replace('(', '').replace(')', '').split(', ')
		i = get_color_escape(i[0], i[1], i[2])
		ft+=f"{i}{text[col]}"
		col+=1
	print(ft, end="")
	print(RESET)
