# To Be And Not To Be

Problem:
```bash
we've got a funky shell over here, and we're going to feed it your input!
the shell will run the following:
console.log(%s !== (%s));
And the flag is `flag{<md5>}, where <md5> is the md5sum of the input that prints true!
```

Looking on Google seems that in JS, the value NaN is of type Number but it is not equal to himself.

Lets hash it with md5 to get the flag.

``` flag{7ecfb3bf076a6a9635f975fe96ac97fd}} ```