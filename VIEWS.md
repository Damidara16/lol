USER (api views, mobile)
edit, create, delete account
list rewards, deals, points, transactions


STORE (web views, website)
edit, create, delete account
view customer details
deactivate customers



CONTENT (web views, website)
list, create, delete | rewards, deals, point plans
list transactions customers
apply rewards to customers
notify users of new rewards



ANALYITICS (web views, website)
list all customers, by join date, age, gender, total money spent, points(ASC, DEC)
list customers that used certain rewards, by join date, age, gender, total money spent, points(ASC, DSC)



REDEEM
validate reward
relocate reward when used
attach reward to transaction



BILLING (web views, website)
adding, remove billing info
webhook for validating plan cycle
updating validation codes in active list
(to validate that a request is from active plan user, active codes will be held in a 'list' and the view will check if code is in active, else return an error)


POINTS ARE AFTER RELEASE


step by step:
1. a client comes to our site, creates an account and chooses a plan
2. a client submits their logo and info for the app
3. we send the app to the client and instructions on how upload to app stores
4. after app has been successfully been uploaded. the user can create a test account on the app
5. the test user requires an sign up process
6. the store can now go online to their web console to create a reward
7. the reward will sent out and applied to the appropriate customers
8. the customer can now check their app for the reward
9. the customer can now apply their reward
method 1:
10.  type in the reward number and customer id to verify if the reward is valid
11. they can now click to use code, which will remove the reward to used, and apply the reward to their transaction  
method 2:
10. when being applied, the store will scan qr code which will provide a reward code that the store enters to apply reward.
11. when used the transaction will be sent to a webhook that will take the store and reward id and customer id to remove the reward to used

how to automate the reward application
generate qr code system
how to attach transaction to customer s

method 1:
create discount in square account automatically and the store applies when the customers show card
method 2:
scan reward and create transaction and apply reward or scan reward to existing transaction and apply reward
option 1:
create a new pos app that links with our app and square account and accepts payments
option 2:
scan reward on our app and redirect info to square default pos app and applies reward

use webhook to attach transactions with customers
