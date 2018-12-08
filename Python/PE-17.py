one_to_nineteen = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
twenty_to_ninety = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
thousand = 8

count = 0

for i in range(1, 1000):
	hang_don_vi = i % 10
	hang_chuc = int((i%100 - hang_don_vi) / 10)
	hang_tram = int((i - hang_chuc*10 - hang_don_vi) / 100)

	if hang_tram != 0:
		count += one_to_nineteen[hang_tram] + hundred
		if hang_chuc != 0 or hang_don_vi != 0:
			count += 3
	if hang_chuc == 0 or hang_chuc == 1:
		count += one_to_nineteen[hang_chuc * 10 + hang_don_vi]

	else:
		count += twenty_to_ninety[hang_chuc] + one_to_nineteen[hang_don_vi]

count += one_to_nineteen[1] + thousand

print(count)