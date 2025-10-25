import configparser

_conf = None


def _get_config_parser() -> configparser.ConfigParser:
    global _conf
    if _conf is not None:
        return _conf
    _conf = configparser.ConfigParser()
    _conf.read('src/config.ini')
    return _conf


conf = _get_config_parser()

__all__ = ['conf']
