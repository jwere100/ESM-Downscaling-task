#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 11:12:41 2025

@author: jwere
"""

import cdsapi

def download_api():
    #part 1 getting the data from cdsapi
    download_path = '/Users/jwere/School/ESM Downscaling Task'
    dataset = "derived-era5-pressure-levels-daily-statistics"
    request = {
        "product_type": "reanalysis",
        "variable": ["temperature"],
        "year": "1988",
        "month": [
            "01", "02", "03",
            "04", "05", "06",
            "07", "08", "09",
            "10", "11", "12"
        ],
        "day": [
            "01", "02", "03",
            "04", "05", "06",
            "07", "08", "09",
            "10", "11", "12",
            "13", "14", "15",
            "16", "17", "18",
            "19", "20", "21",
            "22", "23", "24",
            "25", "26", "27",
            "28", "29", "30",
            "31"
        ],
        "pressure_level": ["1"],
        "daily_statistic": "daily_mean",
        "time_zone": "utc+00:00",
        "frequency": "6_hourly",
        "area": [49, -125, 25, -66]
    }
    client = cdsapi.Client()
    output_path = f"/Users/jwere/School/era5_temperature_1988.nc"
    client.retrieve(dataset, request).download(output_path)
    
    download_path = '/Users/jwere/School/ESM Downscaling Task'
    dataset = "derived-era5-single-levels-daily-statistics"
    request = {
        "product_type": "reanalysis",
        "variable": ["total_precipitation"],
        "year": "1988",
        "month": [
            "01", "02", "03",
            "04", "05", "06",
            "07", "08", "09",
            "10", "11", "12"
        ],
        "day": [
            "01", "02", "03",
            "04", "05", "06",
            "07", "08", "09",
            "10", "11", "12",
            "13", "14", "15",
            "16", "17", "18",
            "19", "20", "21",
            "22", "23", "24",
            "25", "26", "27",
            "28", "29", "30",
            "31"
        ],
        "daily_statistic": "daily_sum",
        "time_zone": "utc+00:00",
        "frequency": "1_hourly",
        "area": [49, -125, 25, -66]
    }
    
    client = cdsapi.Client()
    output_path = f"/Users/jwere/School/era5_precipitation_1988.nc"
    client.retrieve(dataset, request).download(output_path)
    
if __name__ == '__main__':
    download_api()