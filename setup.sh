#
req () {
    pip install -r requirements.txt
}

setupy () {
    sudo python3 install setup.py
}

configfiles () {
    mkdir /home/ubuntu/config
    cp /lib/ialint.json /home/ubuntu/config
    cp /lib/ialdbhierarchy.json /home/ubuntu/config
}

makealiases () {

}

setup () {
    req && configfiles && setupy
    makealiases
}
