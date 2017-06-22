#
req () {
    pip install -r r.txt
}

setupy () {
    sudo python3 install setup.py
}

configfiles () {
    cp /lib/instances.json /home/ubuntu/data
    cp /lib/hierarchy.json /home/ubuntu/data
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

setup
exit(0)
