import re

tweet2 = 'My beautiful sunflowers on a sunny Friday morning off :) #sunflowers #favourites #happy #Friday off…' \
        ' https://t.co/3tfYom0N1i'


# remove old style retweet text "RT"
tweet2 = re.sub(r'^RT[\s]+', '', tweet2)

# remove hyperlinks
tweet2 = re.sub(r'https?://[^\s\n\r]+', '', tweet2)

# remove hashtags
# only removing the hash # sign from the word
tweet2 = re.sub(r'#', '', tweet2)

print(tweet2)