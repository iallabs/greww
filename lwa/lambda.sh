
dbmanager () {
    python /home/ec2-user/projects/licapy-web-api/lwa/databases/_dbmanager.py $0
}

api () {
    python /home/ec2-user/projects/licapy-web-api/lwa/databases/_api.py $0
}

getla () {
    cd /home/ec2-user/projects
    rm -rf licapy-api
    git clone https://github.com/ImperialAlphaLab/licapy-api
}

buildla () {
    cd /home/ec2-user/projects/licapy-api
    python3 setup.py install
}

newla () {
    getla
    buildla
}

testla() {
    cd /home/ec2-user/projects/licapy-api
    python3 setup.py test
}

alias dbmanager='dbm'
