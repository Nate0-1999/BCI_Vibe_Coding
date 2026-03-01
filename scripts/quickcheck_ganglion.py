#!/usr/bin/env python3

import argparse
import time
from pathlib import Path

from brainflow.board_shim import BoardIds, BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Quick stream check for OpenBCI Ganglion.")
    parser.add_argument(
        "--board",
        choices=["ganglion", "ganglion_native"],
        default="ganglion_native",
        help="Board type for BrainFlow connection.",
    )
    parser.add_argument(
        "--serial-port",
        default="",
        help="Serial port for Ganglion dongle mode (example: /dev/cu.usbserial-DM0258P0).",
    )
    parser.add_argument(
        "--mac-address",
        default="",
        help="MAC address for Ganglion native BLE mode.",
    )
    parser.add_argument(
        "--seconds",
        type=int,
        default=10,
        help="Capture duration in seconds.",
    )
    parser.add_argument(
        "--out",
        default="data/raw/quickcheck.csv",
        help="Output CSV path.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    board_id = (
        BoardIds.GANGLION_NATIVE_BOARD.value
        if args.board == "ganglion_native"
        else BoardIds.GANGLION_BOARD.value
    )

    params = BrainFlowInputParams()
    params.serial_port = args.serial_port
    params.mac_address = args.mac_address

    BoardShim.enable_dev_board_logger()
    board = BoardShim(board_id, params)
    print(f"Preparing session for board_id={board_id}...")
    board.prepare_session()
    try:
        print("Starting stream...")
        board.start_stream()
        time.sleep(args.seconds)
        data = board.get_board_data()
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        DataFilter.write_file(data, str(out_path), "w")
        print(f"Wrote {data.shape[1]} samples to {out_path}")
    finally:
        print("Stopping stream and releasing session...")
        try:
            board.stop_stream()
        except Exception:
            pass
        board.release_session()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
