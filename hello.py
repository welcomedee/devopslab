'''
Git Basics:
sudo apt install git
git --version
mkdir project
cd project
nano example.py
python3 example.py
git init
git status
git add .
git commit -m "Message"
git log
--Create a github repo--
git remote add origin https://repo.git
git remote -v
git push origin main/master
git pull origin master
git branch test_branch
git checkout test_branch
--makes changes in the .py file and commit--
git checkout master/main
git merge test_branch

Docker Basics:
docker --version
sudo docker images
sudo docker pull hello-world
sudo docker run hello-world
sudo docker run -p 80:80 -d nginx
sudo docker ps
sudo docker stop container_id

Flas app with docker:
nano app.py
"from flask import Flask, render_template, request
app=Flask(name)
@app.route("/")
def home_page(name=None):
return render_template("index.html",name=name)
if name == 'main':
app.run(host='0.0.0.0',port=5000)
" sudo apt install python3-pip

nano Dockerfile
"FROM python3-alpine3.15
WORKDIR /app
COPY ./app
RUN pip install flask
CMD ["python3","app.py"]

sudo docker build -t myimg:1 .
sudo docker run -p 8000:5000 myimg:1
--docker hub--
sudo docker login -u username
sudo docker tag myimg:1 username/dockerimage
sudo docker push username/dockerimage
docker logout

Jenkins sudo systemctl start jenkins
sudo systemctl status jenkins --check https://localhost:8080-- sudo more ... copy and paste the password -create new item->add github repo link->build a trigger "H/5 ****"->build steps->consol output

sudo apt-get update
sudo docker pull prom/prometheus
sudo docker run -d --name=prometheus \
-p 9090:9090 \
-v ./prometheus.yml:/etc/prometheus/prometheus.yml \
prom/prometheus
sudo docker stop prometheus

[prometheus.yml]
global:
  scrape_interval: 15s
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
prometheus_http_requests_total
prometheus_http_requests_total{handler="/api/v1/query"}
rate(prometheus_http_requests_total{handler="/api/v1/query"}[3m])

sudo docker pull grafana/grafana
sudo docker run -d -p 3000:3000 --name grafana grafana/grafana
sudo docker start prometheus
sudo docker stop prometheus grafana
sudo docker start prometheus grafana

prometheus_http_requests_total{handler="/api/v1/query"}
prometheus_tsdb_wal_fsync_duration_seconds_count
prometheus_build_info
prometheus_http_requests_total
promhttp_metric_handler_requests_total
process_resident_memory_bytes

docker networking

sudo sh get-docker.sh
docker network ls
apt-get install bridge-utils
brctl show
docker run -dt ubuntu bash
docker inspect network_id
docker network ls
go inside c1 -> docker exec -it c1_id bash
apt-get install iputils-ping
ping c2_ip
custom bridge
docker network create custom_bridge
docker network ls
brctl show
docker run -dt --network custom_bridge ubuntu bash
docker network connect custom_bridge 
docker network disconnect custom_bridge id
docker inspect custom_bridge

minikube
sudo usermod -aG docker $USER
newgrp docker
sudo systemctl restart docker
docker ps 
minikube start --driver=docker
minikube status
kubectl get nodes
kubectl run my-pod --image=nginix --restart=Never
kubectl get pod my-pod -o wide
kubectl expose pod my-pod --type=NodePort --port=80 --name=my-service
kubectl get services
minikube service my-service --url
kubectl delete pod my-pod

kubectl create deployment mydeployment --image=nginx --replcas=2
kubectl get pods
kubectl get deployment
kubectl expose deployment my-deployment --type=NodePort --port=80
minikube service my-deployment
kubectl scale deployment mydeplyment --replicas=5
kubectl get pods

'''
