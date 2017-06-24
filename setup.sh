#
req () {
    pip install -r r.txt
}

setupy () {
    sudo python3 install setup.py
}

###################################################

setup () {
    req && setupy
}

#####################################################

setup
exit(0)
