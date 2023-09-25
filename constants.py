# Standard Library
from enum import Enum


class UrlService(Enum):
    URL = "https://5a3d-155-190-18-42.ngrok-free.app"
    REPORT_1 = URL + "/bi/v1/disp/rds/reportData/report/i7E39FA1D451B46D580850BF7BBEB77D8"
    REPORT_2 = URL + "/bi/v1/disp/rds/reportData/report/iCBE21C8C7BB745728455B368E2609788"
    DASHBOARD_1 = URL + "/bi/?perspective=dashboard&pathRef=.public_folders%2FSamples%2F1dashboard&action=view&mode=dashboard&CAMN&ui_appbar=false&ui_navbar=false"
