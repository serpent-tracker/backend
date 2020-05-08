#! /usr/bin/env sh



docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml down -v --remove-orphans # Remove possibly previous broken stacks left hanging after an error
docker-compose -f docker-compose.yml up -d
docker-compose -f docker-compose.yml exec -T backend bash /app/tests-start.sh "$@"
docker-compose -f docker-compose.yml down -v --remove-orphans
