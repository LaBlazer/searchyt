# searchyt  

## Getting started
### Installing
Using pip  
```python -m pip install searchyt```
### Usage
```python
from searchyt import searchyt
syt = searchyt()
res = syt.search("Cute Little Puppy Doing Cute things")

for r in res:
    print(r)
```

Prints:
```python
{'title': 'Cute Little Puppy Doing Cute things', 'author': 'YourUncleMoe', 'id': 'j5a0jTc9S10', 'thumb': 'https://i.ytimg.com/vi/j5a0jTc9S10/hqdefault.jpg'}
{'title': 'Cute Puppies Doing Funny Stuff', 'author': 'Kids And Animals Are The Best', 'id': 'Ce7hJ24a8yM', 'thumb': 'https://i.ytimg.com/vi/Ce7hJ24a8yM/hqdefault.jpg'}
{'title': 'Cutest Puppies Doing Funny Things - Cute Little Puppies Funny Videos | Cute Puppy Dog Compilation', 'author': 'Puppies TV', 'id': 'R7lnqfS1dUA', 'thumb': 'https://i.ytimg.com/vi/R7lnqfS1dUA/hqdefault.jpg'}
...
```
To construct youtube url you can simply append the returned ID to url `https://youtube.com/watch?v=`

* The searchyt instance should be reused since it fetches some headers on initialization. Creating a new instance on each search basically means doubling the requests to the youtube api which could get you blocked fast.
## Contributing
Please read CONTRIBUTING.md for the details on the process of pull request submission.
## License
This project is licensed under the Apache License - see the LICENSE.md file for details
