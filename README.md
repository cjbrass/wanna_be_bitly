# wanna_be_bitly

A quick imitation of bit.ly url shortener written for a technical interview. Takes a url provided by the user and returns a
shortened url that will redirect to the original url. No bells and whistles on the UI, and the only validation is that the
provided url is a valid url. Included time stamps on each redirect to allow for cleaning up at a later date.

I attempted to build this quickly, but still did it modularly so that things could be changed and improved in the
future. For example, the generation of the shortened url just randomly generates a string, checks if it exists, and if
it does it generates another 1 character longer. This could cause a lot of database hits, or maybe we want to use some
kind of hash table so that identical url's get the same shortened url. Whatever change may be wanted, it should be easy
to implement.

Worth noting, this will only work for http and https sites, so if the user wanted to use this for an ftp url my code
would put an http:// in front of it (and would then fail validation). The easy solution is to limit this to http and
https protocols only, otherwise I would need to change how the redirect is done to remedy this.