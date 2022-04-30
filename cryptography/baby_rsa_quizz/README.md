# Baby RSA Quizz


RSA explanation:
```bash
RSA is a public-key (asymmetric) cryptosystem named after its creators: Ronald Rivest,
Adi Shamir, and Leonard Adleman). Because this is an assymetric system, there exists two keys: 
a public key (shared openly) and a private key (kept secret). On the other hand, for a symmetric 
cryptosystem like AES, a private key is shared between both parties. For our case, the sender 
encrypts their message with the receiver's public key and the receiver decrypts the sender's 
encrypted message with the private key corresponding to the public key used by the sender.

Press Enter to continue...
________________________________________________________________________________________________

Let's say Bob wants to send a message to Alice using this RSA encryption scheme. Bob needs 
Alice's public key in order to encrypt his message and send it to Alice. 


  Bob                                              Alice
                                          
 /(...                                            ,-"=-.
/ ,-(_`;                                         .       \
\ )_  _;                   n, e                  "='"=\   '
(\[_][_])        <=======================        `@] @'|   )
 |  L  |                                         ) ` ' ),-`
 | \-_/                                           \^_,  \,  
 | |                                                ,(\,/ )`-. 


An RSA public key is comprised of two integers: n and e

        n: public modulus
        e: public exponent 


Press Enter to continue...
________________________________________________________________________________________________

Now Bob has the facilities to send Alice a message. Bob now sends the ciphertext (ct) 
using his plaintext (pt) represented as an integer and Alice's public key such that: 
ct = (pt)^e mod n.


  Bob                                              Alice
                                          
 /(...                                            ,-"=-.
/ ,-(_`;                                         .       \
\ )_  _;            ct = (pt)^e mod n            "='"=\   '
(\[_][_])        =======================>        `@] @'|   )
 |  L  |                                         ) ` ' ),-`
 | \-_/                                           \^_,  \,  
 | |                                                ,(\,/ )`-. 


Alice now has Bob's encrypted message and uses her private exponent (d) to decrypt 
the message such that: pt = (ct)^d mod n.

An RSA private key is comprised of two integers: d and n

        n: public modulus
        d: private exponent 


Press Enter to continue...
________________________________________________________________________________________________

Let's talk about the key generation of RSA and some of the properties of secure RSA. Typically, 
secure RSA parameters includes the use of 2048-bit or 4096-bit prime numbers. If don't know how 
big 2048/4096-bit values are give this a nice run in Python:


>>> from Crypto.Util.number import getPrime
>>> getPrime(2048)


Here is a rough outline of how RSA keys are generated:
        - Generate prime number p
        - Generate prime number q
        - n = p*q
        - λ(n) = lcm(λ(p), λ(q)) = lcm(p-1, q-1)
        - 1 < e < λ(n) s.t. gcd(e, λ(n)) = 1 (aka. e and λ(n) are coprime)
                - the most common value for e is 2^16 + 1 = 65537
                - the fastest value for e is 3, but this isn't totally secure in some settings.
        - calculate d s.t. d*e = 1 (mod λ(n))

Sick! Now we have everything needed for our public and private keys.

Reminder:
        - Public Key: (n,e)
        - Private Key: (n,d)
                - p, q, λ(n) are kept secret since these values are used to calculate the secret key.

This keypair is now ready for use. 

Press Enter to continue...
________________________________________________________________________________________________

One of the main security notions surrounding RSA is simply the fact that factoring n is a **hard** problem.
It straight up takes way too much computational power to factor a large number such as n.
Although using numbers this large makes us secure against today's computational power, RSA is considered slow 
in the world of Cryptography because of the number crunching it takes for doing modular exponentiation compared 
to that of block ciphers and other encryption schemes that have quicker security mechanisms. Funnily enough, 
assymetric cryptography is mainly used to send symmetric keys instead of sharing data. 

Press Enter to continue...
________________________________________________________________________________________________

Now, hopefully you understand the basic cogs of the RSA machine and some of the math behind it. Unfortunately, 
RSA isn't always implemented correctly, opening the possibility of attacks. As you work your way through this quiz, 
I recommend using some prett nice Python crypto/number libraries: gmpy/gmpy2, pycryptodome, binascii, and pwntools. 
The three parts to the quiz each have a primitive attack on an improper implementation of RSA. Solve all 3 to get 
the flag. Удачи!

Press Enter to exit back to main menu
```


Quizz:
```bash
I see you are ready to take my quiz! This quiz is comprised of three parts with 
each part giving you a poor implementation of RSA. If you are unfamiliar with any 
of these values given, it might be worthwhile to check out option 0 in the main 
menu.

 ---------
| Part 1: |
 ---------
n = 163331836668283
e = 65537
ct = 29620184035743

What is the plaintext (in integer form)? 1751476325

___________________________________________________________________________________

Nice job on the first part! Those numbers weren't really as big as we thought. 

 ---------
| Part 2: |
 ---------
n = 18786335819952151754809394526741063851636548936726051481723116745943010508237973471962276676172217623865187323764772575916585550386465648024269687019253708651898118230604414640373661646505433702610657753890251667009229960460851639475840259958089424544160997748246269707570044575464805634214113583566579631948005064376741827815229759975682741682368893314844962983671734746660109187390345413011080956498816867657931708160164848264117343614948153061614005708051665354613544445951299122140085483006742316654705862919015409751854828885422356496482427068654485238034263229272246713503890496365605594056236730565706808136473
e = 3
ct = 26480272848384180570411447917437668635135597564435407928130220812155801611065536704781892656033726277516148813916446180796750368332515779970289682282804676030149428215146347671350240386440440048832713595112882403831539777582778645411270433913301224819057222081543727263602678819745693540865806160910293144052079393615890645460901858988883318691997438568705602949652125

What is the plaintext (in integer form)? 298062599825784604055397390266655425259311588881437826967301557850952291872230439875703282133697119479127924133583415243365

___________________________________________________________________________________

The small-e attack is a classic! Although making e = 3 may make calculations 
quicker, it is definitely not secure.

 ---------
| Part 3: |
 ---------
q = p + 2
while !(isPrime(q)):
    q += 2
n = p*q


n = 48392146238565018683681028025112430229192546851827881920832779164520976544400427708621200644669460256965473457541641326424397323488462201218408178402115401342900466422693857567615548854554288164463611377745385910935578820608142432826069541454568786297349131419958492123707886201882496841643636052644367498773
e = 65537
ct = 14035064249717668995396909542586138611019707570518679709392852201301164423799344449300684318709605922571960674903934850872176296451070657156699309989799285805431876068098479306458582308704265797551582639897946610059304007764713744060249428603357096541504079768161596289928619016098983608918600914594084616262

What is the plaintext (in integer form)? 
```

To find the answer I used [dcode.fr](dcode.fr) for the first two part.

For the third part dcode won't work, other online tool don't work.

I tried [PollardRsaCracker](https://github.com/ZeroBone/PollardRsaCracker)

Answers are:
* 1751476325
* 298062599825784604055397390266655425259311588881437826967301557850952291872230439875703282133697119479127924133583415243365