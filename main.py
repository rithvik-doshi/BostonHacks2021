import userinfo as u_i
import depression as dp

user_x = u_i.get_userinfo()
print(user_x)
dp.depression(user_x[0])