#密碼重設程式

#先在程式碼中 設定好密碼 password = 'a123456'
#讓使用者[最多輸入3次密碼]
#不對的話, 就印出"密碼錯誤! 還有_次機會"
#對的話, 就印出"登入成功!"

password = 'a123456'
i = 3 #設定機會次數
while i > 0 :
	i = i - 1
	passworD = input('請輸入密碼(a-z,1-9): ')
	if passworD == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!')
		if i > 0 :
			print('還有', i, '次機會')
		else:
			print('請至臨櫃洽詢辦理')

		

