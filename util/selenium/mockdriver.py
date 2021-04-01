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

            def __repr__(self):
                logger.info(f"mocking attribute .{item}")
                logger.info(f"return None")
                return item

        return Mocker()


if __name__ == "__main__":
    mock = MockWebDriver()
    mock.find(1, 2, 3)
    print(mock.a)
