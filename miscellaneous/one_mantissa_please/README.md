# One Mantissa Please

```bash
we've got a funky shell over here, and we're going to feed it your input!
the shell will run the following:
console.log(%d == (%d + 1));
And the flag is `flag{<md5>}, where <md5> is the md5sum of the smallest integer input that prints true!
```


Looks like JS again here we have to play with the floating point representation in JS.

In that case the correct answer is: '9999999999999999'. But this does not give the correct flag.

It seems like '9007199254740991' is the greatest integer in JS and '9007199254740992' answers correct but the hash does not work.

Lets retry later.