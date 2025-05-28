import unittest

# Constants for returning the pile in which the box belongs
STANDARD = "STANDARD"
SPECIAL = "SPECIAL"
REJECTED = "REJECTED"
INVALID_INPUT = "INVALID_INPUT"


def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    :param width: The width of the box, in cm
    :param height: The height of the box, in cm
    :param length: The length of the box, in cm
    :param mass: The mass of the box, in kg
    :return: The string name of the pile that the box is sorted into
    """
    bulky = False
    heavy = False

    # making sure all inputs are either int or float
    if not all(isinstance(x, (int, float)) for x in [width, height, length, mass]):
        return INVALID_INPUT

    # Since bools resolve to True in the above check we do the same for bools to make sure inputs are good
    if any(isinstance(x, bool) for x in[width, height, length, mass]):
        return INVALID_INPUT

    if min(width, height, length, mass) <= 0:
        return INVALID_INPUT

    box_volume = width * height * length

    if max(width, height, length) >= 150 or box_volume >= 1000000:
        bulky = True

    if mass >= 20:
        heavy = True

    if bulky and heavy:
        return REJECTED
    elif bulky or heavy:
        return SPECIAL
    else:
        return STANDARD


class TestSort(unittest.TestCase):
    def test_invalid_inputs(self):
        self.assertEqual(sort(-1, 11, 1, 19), INVALID_INPUT)
        self.assertEqual(sort(5, -11, 1, 1), INVALID_INPUT)
        self.assertEqual(sort(5, 11, -1, 1), INVALID_INPUT)
        self.assertEqual(sort("apple", 11, 1, 0), INVALID_INPUT)
        self.assertEqual(sort(5, 5, True, 1), INVALID_INPUT)
        self.assertEqual(sort(5, 5, 5, [1,1]), INVALID_INPUT)
        self.assertEqual(sort({}, 5, 5, 5), INVALID_INPUT)
        self.assertEqual(sort(5, None, 5, 18), INVALID_INPUT)

    def test_valid_inputs_standard(self):
        self.assertEqual(sort(5, 5, 2, 15), STANDARD)
        self.assertEqual(sort(1, 1.23, 2, 5), STANDARD)
        self.assertEqual(sort(145, 5, 2, 15), STANDARD)
        self.assertEqual(sort(149.999, 5, 50, 7), STANDARD)
        self.assertEqual(sort(5, 5, 149, 19.5), STANDARD)
        self.assertEqual(sort(5, 5, 2, .01), STANDARD)

    def test_valid_inputs_special(self):
        self.assertEqual(sort(155, 5.6, 2, 15), SPECIAL)
        self.assertEqual(sort(147, 500.23, 189, 5), SPECIAL)
        self.assertEqual(sort(140, 5, 20, 25.5), SPECIAL)
        self.assertEqual(sort(149, 149, 149, 19.99), SPECIAL)

    def test_valid_inputs_rejected(self):
        self.assertEqual(sort(155, 5.6, 2, 21), REJECTED)
        self.assertEqual(sort(152, 500.23, 189, 50), REJECTED)
        self.assertEqual(sort(140, 155, 15, 25.5), REJECTED)
        self.assertEqual(sort(149, 149, 149, 20), REJECTED)


if __name__ == '__main__':
    # ADD NEW TEST CALLS TO sort() HERE
    
    unittest.main()

