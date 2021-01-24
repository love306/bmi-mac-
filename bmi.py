#這是一個判斷您ＢＭＩ狀態的程式
height = input('清輸入您的身高： ')
h = (int(height) * 0.01)
weight = input('請輸入您的體重： ')

bmi = int(weight) / (h * h)

if bmi < 18.5 :
	print('您的ＢＭＩ為')
	print(bmi)
	print('「體重過輕」')
elif bmi >= 18.5 and bmi < 24 :
	print('您的ＢＭＩ為')
	print(bmi)
	print('「正常範圍」')
elif bmi >= 24 and bmi < 27:
	print('您的ＢＭＩ為')
	print(bmi)
	print('「輕度肥胖」')
elif bmi >= 27 and bmi < 30:
	print('您的ＢＭＩ為')
	print(bmi)
	print('「中度肥胖」')
else:
	print('您的ＢＭＩ為')
	print(bmi)
	print('「重度肥胖」')