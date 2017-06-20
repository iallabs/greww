#
req () {
    pip install -r r.txt
}

setupy () {
    sudo python3 install setup.py
}

configfiles () {
    cp /lib/ialint.json /home/ubuntu/jsons
    cp /lib/ialdbhierarchy.json /home/ubuntu/jsons
}


makealiases () {
    bash smalias.sh
}

###################################################

setup () {
    req && configfiles && setupy
    makealiases
}

#####################################################
