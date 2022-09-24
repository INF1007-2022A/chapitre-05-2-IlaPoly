#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	TAX = 0.15
	SOUS_TOTAL = 0
	for element in data:
		SOUS_TOTAL += element[INDEX_QUANTITY] * element[INDEX_PRICE]
	TAXES = SOUS_TOTAL * TAX
	TOTAL = SOUS_TOTAL + TAXES
	bill = f"{name} \n" \
		   f"SOUS TOTAL {SOUS_TOTAL : >15.2f} $ \n" \
		   f"TAXES {TAXES : >20.2f} $ \n" \
		   f"TOTAL {TOTAL : >20.2f} $"

	return bill


def format_number(number, num_decimal_digits):
	dec = abs(number - int(number))
	whole = int(number)
	dec2 = round(dec, num_decimal_digits)
	dec_str = str(dec2)
	dec_str2 = dec_str[1:len(dec_str)]
	whole_str = '{:,}'.format(whole).replace(',', ' ')
	final_str = whole_str + dec_str2
	return final_str

def get_triangle(num_rows):
	border_char = '+'
	triangle_char = 'A'
	width_triangle = 1 + 2 * (num_rows - 1)
	height_rect = 0
	form = (border_char * width_triangle + 2 * border_char)
	while height_rect <= num_rows - 1:
		nb_triangle = triangle_char * height_rect * 2 + triangle_char
		form += '\n' + f"{border_char}{nb_triangle:^{width_triangle}}{border_char}"
		height_rect += 1
	form += '\n' + (border_char * width_triangle + 2 * border_char)
	return form


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
