from util.logging.loghelper import LogHelper
import logging

logger = logging.getLogger(__name__)


class MockWebDriver:
    def __getattr__(self, item):
        class Mocker:
            def __call__(self, *args, **kwargs):
                karguments = [f"{k}={v}" for k, v in kwargs.items()]  # list of "k=v" strings
                arguments = [str(arg) for arg in args]
                arguments.extend(karguments)
                all_arguments = ', '.join(arguments)
                logger.info(f"mocking {item}({all_arguments})")
                return MockWebDriver()

            def __repr__(self):
                logger.info(f"mocking attribute .{item}")
                logger.info(f"return MockWebDriver()")
                return MockWebDriver()

        return Mocker()

    def __iter__(self):
        logger.info("mocking __iter__")
        return iter([self])

    # def __next__(self):
    #     return self


if __name__ == "__main__":
    LogHelper.get_root_logger()
    mock = MockWebDriver()
    logger.info(mock.find(1, 2, 3))
    logger.info(mock.get_driver())
    for x in MockWebDriver():
        logger.info(x)
