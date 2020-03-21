#!/usr/bin/env python3
from fastapi import FastAPI, Form
import uvicorn
import time
import json
import sys
import os
import logging
from lib import kmd_lib


### API CALLS
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Sync Status API. See /docs for all methods"}


@app.get("/api_version")
async def api_version():
    return {"version": "0.0.1"}


@app.get("/sync_stats/{ticker}")
async def ticker_sync_stats(ticker: str = "ALL"):
    return kmd_lib.get_sync_stats(ticker)


@app.get("/sync_start/{ticker}")
async def chain_sync_stats(ticker: str = "ALL"):
    return kmd_lib.start_ticker(ticker)


@app.get("/sync_stop/{ticker}")
async def chain_sync_stats(ticker: str = "ALL"):
    return kmd_lib.stop_ticker(ticker)


@app.get("/sync_start_all/")
async def start_sync_all():
    return kmd_lib.start_all_tickers()


@app.get("/sync_stop_all")
async def api_version():
    return kmd_lib.stop_all_tickers()


@app.get("/clean_folder/{ticker}")
async def chain_sync_stats(ticker: str = "ALL"):
    return kmd_lib.clean_ticker_data(ticker)


@app.get("/clean_assetchain_folders")
async def api_version():
    return kmd_lib.clean_all_ticker_data()


@app.get("/sync_stats_all/")
async def start_sync_all():
    return kmd_lib.get_all_sync_stats()


@app.post("/upload_binary/")
async def upload_binary(*, link : str = Form(...)):
    return kmd_lib.setup_binary(link)



#if __name__ == "__main__":
#    uvicorn.run(app, host="95.217.134.179", port=80)