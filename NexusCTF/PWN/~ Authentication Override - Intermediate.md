> [!abstract] Challenge Description
> > Jerry Vu
> ## 300
> Year 2100. UPDC's defense node runs outdated authentication. Exploit the memory vulnerability to bypass security. Below is a code segment that was retrieved by a spy. Your job is to find the flag.
> 
> ```
> int main() {
>     char password[10];
>     int admin = 0;
>     
>     cout << "Enter password: ";
>     scanf("%s", password);
>     
>     if (admin == 0x11223344) {
>         displayFlag();
>     }
>     
>     return 0;
> }
> ```
> 
> Beware of padding and endianness. The program supposedly runs on an ancient distribution called Ubuntu. Access the challenge [here](http://34.129.100.231:5057/).
> 
> Note: your browser likely escapes non-printable characters or changes your input into a different encoding. Be careful how you drop the payload.
> 
> Flag format is: `NexusCTF{<flag>}`

This is again buffer overflow.
We need to be able to input special characters.
Trying with BurpSuite can get the `223344`, however the `11` character was problematic.


---
> [!failure] Flag: ``
