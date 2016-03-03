# wanna_be_bitly

A quick imitation of bit.ly url shortener written for a technical interview. Takes a url provided by the user and returns a
shortened url that will redirect to the original url. No bells and whistles on the UI, and the only validation is that the
provided url is a valid url. Included time stamps on each redirect to allow for cleaning up at a later date. No tests have
been written yet either, and that may be a worthwhile 30 minutes to invest.

Worth noting, this will only work for http and https sites, so if the user wanted to use this for an ftp url it would pass
validation, but my code would put an http:// in front of it. Would need to improve how the redirect is done to remedy this.