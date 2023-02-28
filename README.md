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

## TODO
1. Refactor tests with more precise fixtures
2. Make soft delete instead of hard delete
3. Figure out the design for locking resources per user
4. Hard code base users and remove register user API (+ open register only for testing mode ?)