# mysql中取长度为LENGTH

select tweet_id from Tweets where LENGTH(content)>15;