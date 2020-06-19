#!/bin/bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000
python3 manage.py runserver 0.0.0.0:8000

