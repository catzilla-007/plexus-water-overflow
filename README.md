# plexus-water-overflow
Water Overflow Problem

## Usage

#### If using pipenv
```shell
    $ pipenv install
    $ pipenv run app --help # for help
    $ pipenv run app --liters=3 --capacity=250 --i=2 --j=1 --display=true
```
`--liters` is for setting how much liters will be poured in the glass pyramid

`--capacity` is for setting what is the capacity of each glass

`--i` and `--j` is for getting what glass to check

`--display` is for illustrating the water overflow distribution

Output

```shell
$ pipenv run app --liters=3 --capacity=250 --i=2 --j=2 --display=true

                                    [(0,0) 250 ml]      

                           [(1,0) 250 ml]      [(1,1) 250 ml]      

                  [(2,0) 250 ml]      [(2,1) 250 ml]      [(2,2) 250 ml]      

         [(3,0) 156.25 ml]      [(3,1) 250 ml]      [(3,2) 250 ml]      [(3,3) 156.25 ml]      

[(4,0) 0 ml]      [(4,1) 171.875 ml]      [(4,2) 250 ml]      [(4,3) 171.875 ml]      [(4,4) 0 ml]      

content in glass[2, 2]: 250 mL
```

### Notes
