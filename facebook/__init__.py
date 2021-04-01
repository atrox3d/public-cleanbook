from .facebook import Facebook
from .mbasicfacebook import MbasicFacebook
from .mfacebook import MobileFacebook

import logging
logger = logging.getLogger(__name__)


class FacebookFactory:
    @staticmethod
    def get_facebook(
            # seleniumhelper,
            # email,
            # password,
            # username,
            *args,
            # facebook_home=None,
            **kwargs
    ):
        # facebook_home = kwargs['facebook_home']
        facebook_home = args[-1]
        if facebook_home.rstrip("/").endswith("www.facebook.com"):
            logger.debug("creating Facebook instance")
            return Facebook(
                # seleniumhelper,
                # email,
                # password,
                # username,
                *args,
                **kwargs
            )
        elif facebook_home.rstrip("/").endswith("mbasic.facebook.com"):
            logger.debug("creating MbasicFacebook instance")
            return MbasicFacebook(
                # seleniumhelper,
                # email,
                # password,
                # username,
                *args,
                **kwargs
            )
        elif facebook_home.rstrip("/").endswith("m.facebook.com"):
            logger.debug("creating MbasicFacebook instance")
            return MobileFacebook(
                # seleniumhelper,
                # email,
                # password,
                # username,
                *args,
                **kwargs
            )
        else:
            raise NotImplementedError(f"the class for {facebook_home} is not yet implemented")
