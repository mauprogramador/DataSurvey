# cSpell:disable
from flask import Flask, request, Response, send_file
import requests
import json
import csv
import os


app = Flask(__name__)
URL = "https://api.elsevier.com/content/search/scopus"
TYPE = "application/json"
HEADERS = lambda apikey: {"Accept": TYPE, "X-ELS-APIKey": apikey}
FIELDS_VALUES = "title,authors,publicationName,coverDate,authkeywords,volume"
DATE_VALUE = "2018-2022"
PATH = "static/results.csv"


if not os.path.exists("static"):
    os.mkdir("static")
if os.path.exists(PATH):
    os.remove(PATH)


def get_response(data: dict = None, code: int = 200) -> Response:
    HEADERS = {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials": True, "Content-Type": TYPE}
    if data is None:
        return Response(None, code, HEADERS, mimetype=TYPE)
    return Response(json.dumps(data, indent=2), code, HEADERS, mimetype=TYPE)


@app.route("/scopus-api")
def scopus_api():
    global URL, HEADERS, FIELDS_VALUES, DATE_VALUE
    if request.method == "GET":

        apikey = request.args.get("apikey")
        if apikey is None or len(apikey) == 0:
            return get_response({"message": "API-Key not found"}, 400)

        keywords = request.args.get("keywords")
        if keywords is None or len(keywords) == 0:
            return get_response({"message": "keywords not found"}, 400)

        keywords = keywords.split(",")
        keywords = [keyword for keyword in keywords if (len(keyword) > 1) and (not keyword.isspace())]
        QUERY_VALUES = " AND ".join(keywords)

        url = f"{URL}?query=TITLE-ABS-KEY({QUERY_VALUES})&field={FIELDS_VALUES}&date={DATE_VALUE}"
        requisition = requests.get(url, headers=HEADERS(apikey))
        if len(requisition.text) == 0:
            return get_response({"message": "error in returning response"}, 200)

        response = json.loads(requisition.text.encode("utf-8"))
        total_results = response["search-results"]["opensearch:totalResults"]
        if int(total_results) == 0:
            return get_response({"message": "none articles has been found"}, 200)

        def map_result(params: dict) -> dict:
            return {
                "Title": params.get("dc:title"),
                "Publication Name": params.get("prism:publicationName"),
                "Date": params.get("prism:coverDate"),
                "Volume": params.get("prism:volume"),
                "URL": params.get("prism:url"),
            }

        response_results: list = response["search-results"]["entry"]
        results_dicts = [map_result(result) for result in response_results]
        # print(json.dumps({"Results": results_dicts}, sort_keys=True, indent=2, separators=(",", ": ")), "\n")

        with open(PATH, "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(["Title", "Publication Name", "Date", "Volume", "URL"])
            for result in results_dicts:
                writer.writerow(result.values())

        return send_file(PATH, "CSV", True, "results.csv")


app.run(debug=True)
