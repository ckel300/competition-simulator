import sr.robot._version_check  # noqa
from sr.robot.robot import ManualTimestepRobot, AutomaticTimestepRobot as Robot
from sr.robot.camera import (
    MarkerType,
    MARKER_ARENA,
    MARKER_TOKEN_GOLD,
    MARKER_TOKEN_SILVER,
)

__all__ = (
    'Robot',
    'MarkerType',
    'MARKER_ARENA',
    'MARKER_TOKEN_GOLD',
    'ManualTimestepRobot',
    'MARKER_TOKEN_SILVER',
)
