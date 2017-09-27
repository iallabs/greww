# Greww

Ready to use data and networking functions

###### Greww status

(Currently tested under ubuntu and OSX systems)
python version: 3.6.1
mysql version: 5.7 (JSON support)

| Master | Greww-dev | CodeCov |
| --- | --- | --- |
| ![CircleCI](https://circleci.com/gh/iallabs/greww.svg?style=svg&circle-token=6748a7f07d64bb2ee72cbe7201d4ce7106ec5bc9) |[![CircleCI](https://circleci.com/gh/iallabs/greww/tree/greww-dev.svg?style=svg&circle-token=6748a7f07d64bb2ee72cbe7201d4ce7106ec5bc9)](https://circleci.com/gh/iallabs/greww/tree/greww-dev) | [![codecov](https://codecov.io/gh/iallabs/greww/branch/master/graph/badge.svg?token=qiUtFFz1Ei)](https://codecov.io/gh/iallabs/greww) |

## Table of content

- [Greww status](#greww-status)
- [Table of content](#table-of-content)
- [Development progress](#dev-progress)
- [Build](#build)
- [Configuration](#configuration)
- [Examples](#examples)

## Development progress

Greww.data

| feature | devidea | written | tested | implemented |
| --- | --- | --- | --- | --- |
| basics | X | X | X | X |
| ini | X | X | X | X |
| json | X | X | X | X |
| mysql | X | X | X | X |

Greww.ressources

| feature | devidea | written | tested | implemented |
| --- | --- | --- | --- | --- |
| ssh | X | O | O | O |
| curl | X | X | O | O |
| shell | X | X | X | X |
| ping | X | O | O | O |

## build

Build package
```
bash build.sh --build
```

Test package
```
bash build.sh --test [ --noscop ]
```

## Configuration

```
{}
```

## Examples


###
