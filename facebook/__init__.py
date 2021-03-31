from .facebook import Facebook
from .mbasicfacebook import MbasicFacebook

import logging
logger = logging.getLogger(__name__)


class FacebookFactory:
    @staticmethod
    def get_facebook(
            seleniumhelper,
            email,
            password,
            username,
            # profileurl,
            facebook_home="https://www.facebook.com"
    ):
        if facebook_home.rstrip("/").endswith("www.facebook.com"):
            logger.debug("creating Facebook instance")
            return Facebook(
                seleniumhelper,
                email,
                password,
                username,
                # profileurl,
                facebook_home
            )
        elif facebook_home.rstrip("/").endswith("mbasic.facebook.com"):
            logger.debug("creating MbasicFacebook instance")
            return MbasicFacebook(
                seleniumhelper,
                email,
                password,
                username,
                # profileurl,
                facebook_home
            )
        else:
            raise NotImplementedError(f"the class for {facebook_home} is not yet implemented")
