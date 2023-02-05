# Note over Cloud
Personal todo from android app to cloud hosting for data

## Build
```sh
docker compose build
```

## Run
```sh
docker compose up -d
```

## Test
```sh
docker compose exec api python3 -m pytest "app/tests" -p no:warnings --cov="app"
```

## Unmake
```sh
sh down.sh
```