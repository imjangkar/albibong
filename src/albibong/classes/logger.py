import json
import logging
import os
from datetime import datetime, timezone

from scapy.all import wrpcap

from albibong.photon_packet_parser import EventData, OperationRequest, OperationResponse

isUsingLogger = False


def use_logger(value):
    global isUsingLogger
    isUsingLogger = value


class Logger(logging.Logger):
    def __init__(
        self,
        name,
        stdout=False,
        log_to_file=True,
        ignore_event=False,
        ignore_request=False,
        ignore_response=False,
    ):
        super().__init__(name)
        self.ignore_event = ignore_event
        self.ignore_request = ignore_request
        self.ignore_response = ignore_response

        self.file_timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%S")
        log_filepath = os.path.join(
            os.path.dirname(__file__), f"../../../log/log_{self.file_timestamp}.txt"
        )
        os.makedirs(os.path.dirname(log_filepath), exist_ok=True)

        self.setLevel(logging.DEBUG)
        log_formatter = logging.Formatter("%(message)s")

        if log_to_file:
            file_handler = logging.FileHandler(log_filepath, encoding="utf-8")
            file_handler.setFormatter(log_formatter)
            file_handler.setLevel(logging.INFO)
            self.addHandler(file_handler)

        if stdout:
            stdout_handler = logging.StreamHandler()
            stdout_handler.setFormatter(log_formatter)
            stdout_handler.setLevel(logging.INFO)
            self.addHandler(stdout_handler)

        # Load Event and Operation Code for logging
        eventCodeJsonPath = os.path.join(
            os.path.dirname(__file__), "../resources/event_code.json"
        )
        with open(eventCodeJsonPath) as json_file:
            data = json.load(json_file)
            self.event_code = data

        operationCodeJsonPath = os.path.join(
            os.path.dirname(__file__), "../resources/operation_code.json"
        )
        with open(operationCodeJsonPath) as json_file:
            data = json.load(json_file)
            self.operation_code = data

    def get_timestamp(self):
        return datetime.now(timezone.utc).strftime("%H:%M:%S")

    def log_payload(self, payload):
        if not isUsingLogger:
            return

        if type(payload) == EventData:
            self.log_event(payload)
        elif type(payload) == OperationRequest:
            self.log_request(payload)
        elif type(payload) == OperationResponse:
            self.log_response(payload)

    def log_dps_meter_state(self, state: bool):
        text = f"{self.get_timestamp()} DPS METER IS {'RUNNING. The damages below this point will be recorded.' if state else 'PAUSED. The damages below this point will NOT be recorded.'}"
        print(text)
        if isUsingLogger:
            self.info(text)

    def log_event(self, payload: EventData):
        if self.ignore_event:
            return

        # Ignore position update, timesync, and guild updates
        if payload.code == 3:
            return

        parameters = payload.parameters
        if 252 in parameters and parameters[252] in {99, 100, 152}:
            return

        event_code = str(parameters[252]) if 252 in parameters else None
        if event_code in self.event_code:
            event_code = self.event_code[event_code]

        self.info(f"{self.get_timestamp()} event {event_code}")
        self.info(parameters)

    def log_request(self, payload: OperationRequest):
        if self.ignore_request:
            return

        parameters = payload.parameters
        operation_code = str(parameters[253]) if 253 in parameters else None
        if operation_code in self.operation_code:
            operation_code = self.operation_code[operation_code]

        self.info(f"{self.get_timestamp()} request {operation_code}")
        self.info(parameters)

    def log_response(self, payload: OperationResponse):
        if self.ignore_response:
            return

        parameters = payload.parameters
        operation_code = str(parameters[253]) if 253 in parameters else None
        if operation_code in self.operation_code:
            operation_code = self.operation_code[operation_code]

        self.info(f"{self.get_timestamp()} response {operation_code}")
        self.info(parameters)

    def log_error_pcap(self, packet):
        wrpcap(f"../pcap/error_{self.file_timestamp}.pcapng", packet, append=True)
