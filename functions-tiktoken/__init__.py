import logging

import azure.functions as func
import tiktoken


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    text = req.params.get("text")
    if not text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            text = req_body.get("text")

    if text:
        enc = tiktoken.get_encoding(
            "cl100k_base"
        )  # for gpt-3.5-turbo, gpt-4, text-embedding-ada-002
        tokens = enc.encode(text)
        tokens_count = len(tokens)
        logging.info(f"Tokens count: {tokens_count=}")
        return func.HttpResponse(f"{tokens_count}")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a text in the query string or in the request body for a personalized response.",
            status_code=200,
        )
