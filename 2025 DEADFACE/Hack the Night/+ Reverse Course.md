> [!abstract] Challenge Description
> > @syyntax
> ## 60
> One of the accounts that DEADFACE compromised was an admin-level user. NVU has since removed the account, but there still might be information about the account located in the web app. See if you can find the password that belongs to the Emergency Admin user account.
> 
> Submit the flag as `deadface{password}`. Example: `deadface{P@$$w0rd!}`.
> 
> [http://env01.deadface.io:8080](http://env01.deadface.io:8080/)

When logged in as admin, you can view the users on the site. When pressing view details, the url changes to `http://env01.deadface.io:8080/admin.php?view_user={user_id}&source=ui`

Users only go up to 15, but when checking 16, it shows a backup admin account. We find the hashed password `c4ca4238a0b923820dcc509a6f75849b`
Looks like MD5, putting it in a reverse lookup (note that it is a hash and cannot be truly reversed), it results in the string 1. The password is "1"


---
> [!success] Flag: `deadface{1}`
