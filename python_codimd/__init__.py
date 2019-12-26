from pbr.version import VersionInfo

__version__ = VersionInfo('python_codimd').version_string()
__version_info__ = VersionInfo('python_codimd').semantic_version().version_tuple()

from .hello import HelloWorld
