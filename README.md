# searchyt
### Lightweight Python 3 library for searching youtube videos  


Usage:
```
from searchyt import searchyt
syt = searchyt()
res = syt.search("Cute Little Puppy Doing Cute things")

for r in res:
    print(r)
```

Prints:
```
{'title': 'Cute Little Puppy Doing Cute things', 'author': 'YourUncleMoe', 'id': 'j5a0jTc9S10', 'thumb': 'https://i.ytimg.com/vi/j5a0jTc9S10/hqdefault.jpg'}
{'title': 'Cute Puppies Doing Funny Stuff', 'author': 'Kids And Animals Are The Best', 'id': 'Ce7hJ24a8yM', 'thumb': 'https://i.ytimg.com/vi/Ce7hJ24a8yM/hqdefault.jpg'}
{'title': 'Cutest Puppies Doing Funny Things - Cute Little Puppies Funny Videos | Cute Puppy Dog Compilation', 'author': 'Puppies TV', 'id': 'R7lnqfS1dUA', 'thumb': 'https://i.ytimg.com/vi/R7lnqfS1dUA/hqdefault.jpg'}
...
```