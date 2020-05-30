# Note: we don't actually know if webots offers up tuples or lists.
from typing import Tuple, Sequence


class CameraRecognitionObject:
    def get_id(self) -> int: ...
    def get_position(self) -> Tuple[float, float, float]: ...
    def get_orientation(self) -> Tuple[float, float, float, float]: ...
    def get_size(self) -> Tuple[float, float]: ...
    def get_position_on_image(self) -> Tuple[int, int]: ...
    def get_size_on_image(self) -> Tuple[int, int]: ...
    def get_number_of_colors(self) -> int: ...
    def get_colors(self) -> Sequence[float]: ...
    def get_model(self) -> bytes: ...