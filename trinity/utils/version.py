import sys

import pkg_resources

from trinity import __version__


def construct_trinity_client_identifier() -> str:
    """
    Constructs the client identifier string

    e.g. 'Trinity/v1.2.3/darwin-amd64/python3.6.5'
    """
    return "Trinity/{0}/{platform}/{imp.name}{v.major}.{v.minor}.{v.micro}".format(
        __version__,
        platform=sys.platform,
        v=sys.version_info,
        # mypy Doesn't recognize the `sys` module as having an `implementation` attribute.
        imp=sys.implementation,  # type: ignore
    )


def is_prerelease() -> bool:
    try:
        distro = pkg_resources.get_distribution("trinity")
        # mypy thinks that parsed_version is a tuple. Ignored...
        return distro.parsed_version.is_prerelease  # type: ignore
    except pkg_resources.DistributionNotFound:
        return True
