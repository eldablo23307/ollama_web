from .app import app


def main() -> None:
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    main()
