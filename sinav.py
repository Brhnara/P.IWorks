##QUESTION 3
a=10
b=5

a, b = b, a
print(a)
print(b)

##QUESTION 4
SELECT i_users.username, COUNT( i_user_login_logs.login_date ) AS Number_of_logins 
FROM i_users
INNER JOIN i_user_login_logs ON i_users.userID= i_user_login_logs.userID
WHERE  i_user_login_logs.login_date IN ((select login_date
                                         from i_user_login_logs
                                         group by user_Id
                                         having count(*) > 2))

