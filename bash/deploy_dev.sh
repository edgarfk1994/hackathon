cd ./devops && docker-compose -f localhost.yml up -d && cd ..
sleep 2
uvicorn main:app --reload