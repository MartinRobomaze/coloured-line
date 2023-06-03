find ../data/CD/ -name "*.png" | parallel -I% --max-args 1 python main.py %
