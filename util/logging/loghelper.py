import sys
import logging

logger = logging.getLogger(__name__)


##################################################################################################################
# logging.NOTSET | "NOTSET" | 0:
#       Detailed information, typically of interest only when diagnosing problems.
# logging.DEBUG | "DEBUG" | 10:
#       Detailed information, typically of interest only when diagnosing problems.
# logging.INFO | "INFO" | 20:
#       Confirmation that things are working as expected.
# logging.WARNING | "WARNING" | 30:
#       An indication that something unexpected happened, or indicative of some problem in the near future
#       (e.g. ‘disk space low’). The software is still working as expected.
# logging.ERROR | "ERROR" | 40:
#       Due to a more serious problem, the software has not been able to perform some function.
# logging.CRITICAL | "CRITICAL" | 50:
#       A serious error, indicating that the program itself may be unable to continue running.
##################################################################################################################
class LogHelper:
    FORMAT_STRING = '%(asctime)s | %(levelname)-8s | %(name)-25s | %(funcName)20s() | %(message)s'
    ROOTLOGGER = None

    def __init__(self):
        pass

    @staticmethod
    def get_root_logger(format_string=FORMAT_STRING, level=logging.NOTSET) -> logging.Logger:
        if not LogHelper.ROOTLOGGER:
            logging.basicConfig(level=level, format=format_string)
            logger.info("root logger configured.")
            LogHelper.ROOTLOGGER = logging.getLogger()
        return LogHelper.ROOTLOGGER

    @staticmethod
    def get_cli_logger(
            name=None,                  # root logger by default
            level=logging.DEBUG,
            set_handler=True,
            format_string=FORMAT_STRING,
            output_stream=sys.stderr,
    ) -> logging.Logger:
        """
        ########################################################################################################################
            - GET LOCAL (NON-ROOT) LOGGER INSTANCE THAT OUTPUTS TO CLI
            - SET LEVEL TO DEBUG (DEFAULT IS WARNING)
        ########################################################################################################################
        """
        _logger = logging.getLogger(name)  # get local logger
        _logger.setLevel(level)  # set logger level >= logger_level
        """
        ########################################################################################################################
            - GET SAME FORMATTER INSTANCE FOR ALL HANDLERS
        ########################################################################################################################
        """
        format_string = format_string
        formatter = logging.Formatter(format_string)  # get formatter
        """
        ########################################################################################################################
            - GET CLI HANDLER INSTANCE
            - SET FORMATTER FOR CLI HANDLER INSTANCE
            - ADD HANDLER TO LOCAL LOGGER
        ########################################################################################################################
        """
        if set_handler and not _logger.hasHandlers():
            if isinstance(output_stream, str):
                # by stream name
                try:
                    output_stream = {stream.name.strip("<>"): stream for stream in (sys.stderr, sys.stdout)}[output_stream]
                    logger.debug(f"assigning {output_stream.name} to handler")
                except KeyError as ke:
                    print(f"stream '{output_stream}' not found, setting sys.stderr")
                    output_stream = sys.stderr
            elif not isinstance(output_stream, type(sys.stderr)):
                # by stream
                print(f"{output_stream} is not a {type(sys.stderr)}")
                output_stream = sys.stderr

            cli_handler = logging.StreamHandler(stream=output_stream)   # get CLI handler (default=stderr)
            cli_handler.setFormatter(formatter)                         # set formatter for CLI handler
            _logger.addHandler(cli_handler)                             # add CLI handler to logger

        return _logger

    @staticmethod
    def list_loggers(condition_name=None, condition_value=None):
        loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
        if condition_name:
            loggers = [_logger for _logger in loggers if getattr(_logger, condition_name) == condition_value]
        # print(loggers)
        return loggers

    @staticmethod
    def list_logger_names():
        logger_names = [logging.getLogger(name).name for name in logging.root.manager.loggerDict[:]]
        # print(loggers)
        return logger_names

    @staticmethod
    def disable_loggers(*prefixes):
        for prefix in prefixes:
            for current_logger in LogHelper.list_loggers():
                if current_logger.name.startswith(prefix):
                    logger.debug(f"disabling {current_logger.name}")
                    current_logger.disabled = True

    @staticmethod
    def list_disabled_loggers():
        return LogHelper.list_loggers("disabled", True)

    @staticmethod
    def list_enabled_loggers():
        return LogHelper.list_loggers("disabled", False)


if __name__ == "__main__":
    LogHelper.get_cli_logger(output_stream=LogHelper)
    LogHelper.get_cli_logger(output_stream="ciao")
