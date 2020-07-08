from flask import Flask
import threading
import time

def intense_cpu():
    def run():
        while True:
            print('thread running')
            global stop_threads
            if stop_threads:
                break

    threads = []

    for i in range(10):
        t1 = threading.Thread(target=run)
        t1.start()

    time.sleep(10)
    global stop_threads
    stop_threads = True
    for thread in threads:
        thread.join()
    print('threads were killed')

stop_threads = False
app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    return "Hello World!", 200

@app.route('/intense',methods=['GET'])
def intense():
    intense_cpu()
    return ""

if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0', debug=True)

