#!/bin/bash
echo "Gerando cobertura..."
docker compose exec backend coverage run -m pytest
docker compose exec backend coverage xml

echo "Executando análise SonarQube..."
docker run --rm --network backend_default -v $(pwd):/usr/src sonarsource/sonar-scanner-cli

echo "Análise concluída! Verifique http://localhost:9000"
