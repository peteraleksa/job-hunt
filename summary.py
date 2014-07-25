import json
import nltk

with open('posts.json', 'r') as infile:
    posts = []
    for line in infile:
        posts.append(json.loads(line))

for post in posts:
    print '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print ''.join(post['title']) + ' Posted: ' + ''.join(post['posted'])
    print '\n'
    print ''.join(post['original_post_link'])
    print 'Keywords:'
    print post['keywords']
    print '\nSummary: \n'
    text = nltk.Text(post['tokenized_text'])
    print ' '.join(text[0:100]) + '\n'