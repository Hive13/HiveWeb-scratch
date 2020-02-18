from app import app

#* set debut to False for prod
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    