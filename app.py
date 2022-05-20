import logging
import os

import joblib
from azure.storage.blob import BlobClient, __version__
from flask import (
    Flask,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)

from helper import eval_model, load_housing_data

app = Flask(__name__)

MODEL_PATH = os.path.join("artifacts", "best_model.pkl")


def configure_log():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/log.log",
        level=logging.DEBUG,
        format=f'{"%(asctime)s %(levelname)s %(threadName)s : %(message)s"}',
    )


def get_artifacts():
    container = "hpp-flask-app"
    model_blob = "artifacts/best_model.pkl"
    data_blob = "data/test.csv"
    app.logger.info(
        "Azure Blob Storage v" + __version__ + " - Python quickstart sample"
    )

    connect_str = "DefaultEndpointsProtocol=https;AccountName=storageaccountombhuyan;AccountKey=n1qicd6RN7+0pnOI8BDubKl1jrbikYbPmMoNNUVtj1zA6Zuzhaj/m0Eowzi8uNcxZF+VEyEbI7YY+AStzCO32g==;EndpointSuffix=core.windows.net"
    """Create the BlobServiceClient object which
    will be used to create a container client"""
    # blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    app.logger.info("Connection stablish.")
    """Get a client to interact with a specific
    container - though it may not yet exist"""
    # container_client = blob_service_client.get_container_client(container)
    model_blob_client = BlobClient.from_connection_string(
        connect_str, container, model_blob
    )

    if not os.path.exists(MODEL_PATH):
        app.logger.info("Start downloading model ...")
        model_downloader = model_blob_client.download_blob()

        os.makedirs("artifacts", exist_ok=True)
        with open(MODEL_PATH, "wb") as model_file:
            model_file.write(model_downloader.readall())
        app.logger.info("Download Complete")
    else:
        app.logger.info("Model present locally.")

    data_blob_client = BlobClient.from_connection_string(
        connect_str, container, data_blob
    )
    data_url = data_blob_client.url
    return data_url


@app.route("/", methods=["GET", "POST"])
def home():
    # return "Hello, world!"
    if request.method == "POST":

        if request.form["action"] == "Check Score":
            app.logger.info("Checking score...")
            return redirect(url_for("score"))

        elif request.form["action"] == "Check Prediction":
            app.logger.info("Checking prediction...")
            return redirect(url_for("predict"))
    return render_template("index.html")


@app.route("/score")
def score():
    rmse, mae, r2 = eval_model(model, test_data)
    score = {"rmse": rmse, "mae": mae, "r2": r2}
    return render_template("score.html", data=score)


@app.route("/predict")
def predict():
    housing_prepared_test = test_data.drop("median_house_value", axis=1)
    # test_actual = test_data["median_house_value"]
    pred = model.predict(housing_prepared_test)
    housing_prepared_test["Predicted Price"] = pred
    predict_table = housing_prepared_test.iloc[:, 1:].to_html(
        classes="tbl-header", header=True, index=False
    )
    return make_response(
        render_template("predict.html", tables=[predict_table])
    )


if __name__ == "__main__":
    configure_log()
    app.logger.info("App Started.")
    test_data_url = get_artifacts()
    model = joblib.load(MODEL_PATH)
    test_data = load_housing_data(test_data_url)

    app.run(host="0.0.0.0", port=5000)
