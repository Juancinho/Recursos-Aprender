from pathlib import Path
import csv

OUT = Path(__file__).resolve().parents[1] / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
REQ = OUT / "requirements.csv"
TESTS = OUT / "tests.csv"

requirements = [
    ("REQ-UDS-001", "diagnostics", "The ECU shall support UDS service 0x22 ReadDataByIdentifier."),
    ("REQ-UDS-002", "diagnostics", "The diagnostic module shall return NRC 0x31 when the DID is unsupported."),
    ("REQ-CAN-001", "can", "The body controller shall transmit status frame 0x120 every 10 ms."),
    ("REQ-CAN-002", "can", "The gateway shall reject CAN frames with invalid DLC."),
    ("REQ-DOIP-001", "doip", "The tester shall establish a DoIP TCP connection before diagnostic requests."),
    ("REQ-LGT-001", "lighting", "The vehicle shall turn on low beam when ambient light is below threshold."),
    ("REQ-BODY-001", "body", "The central locking system shall unlock all doors after a valid remote command."),
    ("REQ-DIAG-003", "diagnostics", "The ECU shall respond within 50 ms to supported diagnostic requests."),
]

tests = [
    ("TC-UDS-001", "REQ-UDS-001", "Send 0x22 for a supported DID and verify positive response."),
    ("TC-UDS-002", "REQ-UDS-002", "Send 0x22 for an unsupported DID and verify NRC 0x31."),
    ("TC-CAN-001", "REQ-CAN-001", "Measure period of CAN ID 0x120 over 5 seconds."),
    ("TC-DOIP-001", "REQ-DOIP-001", "Open DoIP TCP connection and send routing activation."),
    ("TC-LGT-001", "REQ-LGT-001", "Simulate low ambient light and verify low beam output."),
]

def write_csv(path, header, rows):
    if path.exists():
        print(f"{path} already exists; not overwriting.")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"Created {path}")

write_csv(REQ, ["requirement_id", "module", "text"], requirements)
write_csv(TESTS, ["test_id", "covers", "text"], tests)
print("Dataset ready in 13_Labs/outputs/")
