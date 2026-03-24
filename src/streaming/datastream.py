from pylsl import StreamInlet, resolve_byprop


def main():

    # Search for active LSL streams
    streams = resolve_byprop("type", "EEG", timeout=10)
    if len(streams) == 0:
        raise RuntimeError("Can't find EEG stream.")

    # Set active EEG stream to inlet and apply time correction
    print("Start acquiring data.")
    inlet = StreamInlet(streams[0])
    eeg_time_correction = inlet.time_correction()

    # Get the stream info and description
    info = inlet.info()
    desc = info.desc()
    print(info)
    print(desc)

    # Get the sampling frequency
    fs = int(info.nominal_srate())

    # Get the data (sample = data values (, ts = timestamp(s))
    sample, ts = inlet.pull_sample()
    print(ts, sample)


if __name__ == "__main__":
    main()