from flask import Flask, render_template, url_for, request
from threading import Thread
import psutil

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/home/", methods=["GET"])
def Home_Page():
    CPU_USAGE = psutil.cpu_percent(0.3)
    CPU_CORE = psutil.cpu_count()
    CPU_CORE_MAX_HZ = list(psutil.cpu_freq())
    CPU_CORE_CURRENT_HZ = int(CPU_CORE_MAX_HZ[0])

    return render_template("home.html", CPU_USAGE=CPU_USAGE, CPU_CORE=CPU_CORE, CPU_CORE_HZ=CPU_CORE_MAX_HZ, CPU_CORE_CURRENT_HZ=CPU_CORE_CURRENT_HZ)

@app.route("/home/test/", methods=["POST"])
def test():
    if request.method == "POST":
        return render_template('chatbot.html')
    else:
        return "Invalid" 
if __name__ == "__main__":
    app.run(debug=True)