import coloredlogs
import logging

coloredlogs.install()

LOG_FILENAME = "app.log"
logging.basicConfig(
    filename=LOG_FILENAME,
    force=True,
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
)

log = logging.getLogger(__name__)


def main():
    log.info("Done")
    pass


if __name__ == "__main__":
    main()
