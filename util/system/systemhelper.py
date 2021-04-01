import subprocess
import logging

logger = logging.getLogger(__name__)


class SystemHelper:

    @staticmethod
    def run(command: str):
        try:
            logger.info(f'executing "{command}"')
            output = subprocess.check_output(command)
            logger.info(output.decode('utf-8').strip())
        except Exception as e:
            logger.error(e)

    @staticmethod
    def tasklist(imagename="chromedriver.exe"):
        # os.system(f'tasklist /FI "IMAGENAME eq {imagename}"')
        SystemHelper.run(f'tasklist /FI "IMAGENAME eq {imagename}"')

    @staticmethod
    def taskkill(imagename="chromedriver.exe"):
        # os.system(f'taskkill /F /IM {imagename}')
        SystemHelper.run(f'taskkill /F /IM {imagename}')
