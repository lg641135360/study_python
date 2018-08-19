'''
    一段小程序
'''

account = "hugao"
password = '123'

print('please input your account')
user_account = input()
print('please input your password')
user_password = input()

if user_account == account and user_password == password :
    print('success')
else :
    print('fail')