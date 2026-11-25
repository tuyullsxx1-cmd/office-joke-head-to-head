import sys

LINE = "Our standup is fifteen minutes because nobody stands up for anything in this office \u2014 least of all the Wi-Fi, which has been down since Tuesday and still gets invited to every meeting."


def main():
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as handle:
            handle.write(LINE)
    except OSError as exc:
        sys.stderr.write("cannot write entry.txt: %s\n" % exc)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
