from flask import Flask

from app.url_info_db import getURLInfo

app = Flask(__name__)

@app.route( '/urlinfo/1/<hostname_and_port>/<original_path_and_query_string>')
def get_url_information(hostname_and_port, original_path_and_query_string):
    malware_info = getURLInfo(hostname_and_port)
    if not malware_info:
        malware_info = "NOT_MALWARE"
    return malware_info


if __name__ == '__main__':
    app.run(debug=True, port=9000)
